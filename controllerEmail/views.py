from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework import status
from .models import EmailTracker, EmailTracking
from django.core.mail import EmailMultiAlternatives
from rest_framework import generics
from .serializer import EmailTrackerSerializer
from django.http import HttpResponse
from PIL import Image
from rest_framework.decorators import api_view
from django.template.loader import get_template
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
import os
import random
from django.shortcuts import get_object_or_404
from django.utils import timezone

class SendTemplateMailView(APIView):
    def post(self, request, *args, **kwargs):
        target_user_emails = request.data.get('email')
        if isinstance(target_user_emails, list):
            target_user_emails = target_user_emails
        elif isinstance(target_user_emails, str):
            target_user_emails = [target_user_emails]
        else:
            return Response({"error": "Invalid email data format"}, status=status.HTTP_400_BAD_REQUEST)

        message = request.data.get('message')
        objet = request.data.get('objet')
        document = request.FILES.get('document', None)

        mail_template = get_template("index.html") 
        context_data_is = dict()

        for email in target_user_emails:
            email_tracker = EmailTracker.objects.create(
                recipient_email=email,
                subject=objet,
                document=document
            )

            # Obtenez l'email_id de l'instance d'EmailTracker actuelle
            email_id = email_tracker.email_id

            # Utilisez email_id pour générer l'URL du tracking pixel
            image_url = self.generate_tracking_pixel_url(request, email_id)
            context_data_is["image_url"] = image_url
            context_data_is["message"] = message
            context_data_is["objet"] = objet

            html_detail = mail_template.render(context_data_is)
            msg = EmailMultiAlternatives(objet, html_detail, 'serignemourtallasyll86@gmail.com', [email])
            msg.content_subtype = 'html'
            msg.attach_file(email_tracker.document.path)
            msg.send()

        return Response({"success": True})

    def generate_tracking_pixel_url(self, request, email_id):
        tracking_pixel_url = request.build_absolute_uri(reverse("tracking_pixel"))
        if email_id:
            tracking_pixel_url += f"?id={email_id}"
        return tracking_pixel_url


class tracking_pixel(APIView):
    def get(self, request):
        email_id = request.GET.get('id')
        if email_id:
            # Recherchez l'instance d'EmailTracker correspondant à l'email_id
            email_tracker = get_object_or_404(EmailTracker, email_id=email_id)
            
            # Mettez à jour le champ opened_at avec le timestamp actuel
            email_tracker.opened_at = timezone.now()
            email_tracker.save()
        
        # Créez une réponse HTTP vide avec un contenu d'un seul pixel transparent
        response = HttpResponse(content_type='image/gif')
        response['Content-Disposition'] = 'inline'
        response.write(b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00;')
        return response


class GetEmailTrackingData(generics.ListAPIView):
    def get_serializer_class(self):
        return EmailTrackerSerializer

    def get_queryset(self):
        return EmailTracker.objects.all()
