from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from .models import EmailTracker, EmailTracking
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from PIL import Image
from rest_framework.decorators import api_view
from django.template.loader import get_template
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from .models import EmailTracking
import os
import random

class SendTemplateMailView(APIView):
    def post(self, request, *args, **kwargs):
        target_user_email = request.data.get('email')
        mail_template = get_template("index.html") 
        context_data_is = dict()
        # Construire l'URL de l'image de suivi avec un paramètre de requête aléatoire
        random_param = f"random={random.randint(1, 100000)}"
        image_url = request.build_absolute_uri(reverse("tracking_pixel")) + '?' + random_param
        context_data_is["image_url"] = image_url
        email_tracker = EmailTracker.objects.create(
            recipient_email=target_user_email,
            subject="Lien de test",
        )
        html_detail = mail_template.render(context_data_is)

        msg = EmailMultiAlternatives("Greetings !!", html_detail, 'serignemourtallasyll86@gmail.com', [target_user_email])
        msg.content_subtype = 'html'
        msg.send()

        return Response({"success": True})


class tracking_pixel(APIView):
    def get(self, request):
        # Créez une réponse HTTP vide avec un contenu d'un seul pixel transparent
        response = HttpResponse(content_type='image/gif')
        response['Content-Disposition'] = 'inline'
        response.write(b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00;')
        
        # Enregistrez l'ouverture de l'e-mail dans la base de données
        email_id = request.GET.get('email_id')
        if email_id:
            try:
                email_tracker = EmailTracker.objects.get(id=email_id)
                email_tracking = EmailTracking.objects.create(email=email_tracker)
                email_tracking.opened_at = datetime.now()
                email_tracking.save()
            except EmailTracker.DoesNotExist:
                pass

        return response


class GetEmailTrackingData(APIView):
    def get(self, request):
        email_id = request.GET.get('email_id')
        email_tracking_data = EmailTracking.objects.filter(email__id=email_id)
        data = [{'opened_at': track.opened_at} for track in email_tracking_data]
        return JsonResponse(data, safe=False)


# class render_image(APIView):
#     def get(self, request):
#         if request.method == 'GET':
#             current_directory = os.path.dirname(os.path.abspath(__file__))
#             image_path = os.path.join(current_directory, 'userAvatar.png')
            
#             # Charger l'image à partir du système de fichiers
#             image = Image.open(image_path)
            
#             # Sauvegarder l'image dans une réponse HTTP
#             image_format = image.format if image.format else 'PNG'  # Utilisez le format d'origine si disponible, sinon PNG
#             response = HttpResponse(content_type=f"image/{image_format.lower()}")
#             image.save(response, image_format)
            
#             email_id = request.query_params.get('email_id')
#             if email_id:
#                 try:
#                     email_tracker = EmailTracker.objects.get(id=email_id)
#                     email_tracking = EmailTracking.objects.create(email=email_tracker)
#                     email_tracking.opened_at = datetime.now()
#                     email_tracking.save()
#                 except EmailTracker.DoesNotExist:
#                     pass
            
#             # Ajouter un paramètre de requête aléatoire à l'URL de l'image
#             random_param = f"random={random.randint(1, 100000)}"
#             image_url = request.build_absolute_uri(reverse("render_image")) + '?' + random_param
            
#             return response