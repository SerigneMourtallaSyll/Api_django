# Import des modules nécessaires
# import smtplib
# import base64
# from email.message import EmailMessage
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.utils import timezone
# from .models import TrackingData
# import json
# from urllib.parse import urlparse, parse_qs
# from django.http import JsonResponse

# # Fonction pour générer l'URL du pixel de suivi avec timestamp
# def generate_open_tracking_pixel(user_id, email_id, timestamp):
#     current_timestamp = int(timezone.now().timestamp())
#     tracking_pixel_url = f"http://127.0.0.1:8000/?user_id={user_id}&email_id={email_id}&timestamp={timestamp}&open_timestamp={current_timestamp}"
#     return tracking_pixel_url


# # Fonction pour envoyer l'e-mail avec le pixel de suivi
# def send_email_with_tracking_pixel(pixel_url, user_id, email_id, timestamp):
#     # Charger la configuration Gmail à partir du fichier JSON
#     with open("config.json") as json_file:
#         gmail_config = json.load(json_file)

#     # Contenu HTML de l'e-mail avec le pixel de suivi
#     html_content = f"""
#         <!DOCTYPE html>
#         <html lang="en">
#         <head>
#             <meta charset="UTF-8">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <title>Test Email</title>
#         </head>
#         <body>
#             <p>Ceci est un test d'e-mail avec un pixel de suivi :</p>
#             <img src="{pixel_url}" width="50px" height="50px" alt="img" />
#         </body>
#         </html>
#     """

#     # Création de l'e-mail
#     msg = EmailMessage()
#     msg['From'] = gmail_config["email"]
#     msg['To'] = "serignemourtallasyll972@gmail.com"
#     msg['Subject'] = 'Test d\'e-mail avec pixel de suivi'
#     msg.set_content(html_content, subtype='html')

#     # Envoi de l'e-mail via SMTP
#     with smtplib.SMTP_SSL(gmail_config["server"], gmail_config["port"]) as smtp:
#         smtp.login(gmail_config["email"], gmail_config["password"])
#         smtp.send_message(msg)
#         print("L'e-mail a été envoyé avec succès.")

# def pixel_tracking(request):
#     # Récupérer les paramètres de requête de l'URL
#     query_params = request.GET
#     user_id = query_params.get('user_id', '')
#     email_id = query_params.get('email_id', '')
#     timestamp = query_params.get('timestamp', '')
#     open_timestamp = query_params.get('open_timestamp', None)

#     # Enregistrer les données de suivi dans la base de données
#     tracking_data = TrackingData.objects.create(
#         user_id=user_id,
#         email_id=email_id,
#         timestamp=timestamp,
#         open_timestamp=open_timestamp,
#         ip_address=request.META.get('REMOTE_ADDR'),
#         user_agent=request.META.get('HTTP_USER_AGENT')
#     )
#     tracking_data.save()

#     # Générer l'URL du pixel de suivi avec timestamp
#     pixel_url = generate_open_tracking_pixel(user_id, email_id, timestamp)
#     print(pixel_url)
#     # Envoyer l'e-mail avec le pixel de suivi
#     send_email_with_tracking_pixel(pixel_url, user_id, email_id, timestamp)

#     # Construire la réponse JSON avec les informations de suivi
#     response_data = {
#         'user_id': user_id,
#         'email_id': email_id,
#         'timestamp': timestamp,
#         'open_timestamp': open_timestamp,
#         'ip_address': tracking_data.ip_address,
#         'user_agent': tracking_data.user_agent,
#         'message': 'Tracking information received successfully.'
#     }

#     # Renvoyer la réponse JSON
#     return JsonResponse(response_data)


# from django.core.mail import send_mail
# from django.http import HttpResponse
# from django.views.generic import View
# from pytracking import Configuration
# from pytracking.django import OpenTrackingView
# import logging
# from datetime import datetime
# import uuid 

# logger = logging.getLogger(__name__)

# class MyOpenTrackingView(OpenTrackingView):
#     def send_tracking_email(self, email_id):
#         # Envoyer l'e-mail contenant le pixel de suivi
#         send_mail(
#             'Test Email',
#             'Test d\'e-mail avec pixel de suivi',
#             'serignemourtallasyll86@gmail.com',
#             ['serignemourtallasyll972@gmail.com'],
#             fail_silently=False,
#         )

#     def send_open_notification(self, email_id, user_agent, user_ip):
#         # Envoyer un e-mail de notification pour l'ouverture de l'e-mail
#         send_mail(
#             'Notification: E-mail ouvert',
#             'L\'e-mail avec l\'ID %s a été ouvert par %s (IP: %s) à %s' % (email_id, user_agent, user_ip, datetime.now()),
#             'serignemourtallasyll86@gmail.com',
#             ['serignemourtallasyll86@gmail.com'],
#             fail_silently=False,
#         )

#     def get(self, request, *args, **kwargs):
#         # Générer un identifiant UUID
#         email_id = uuid.uuid4().hex

#         # Envoyer l'e-mail contenant le pixel de suivi
#         self.send_tracking_email(email_id)

#         # Appeler la méthode parent pour gérer la requête
#         return super().get(request, email_id, *args, **kwargs)

#     def notify_decoding_error(self, exception, request):
#         # Journaliser les erreurs de décodage
#         logger.error("Erreur de décodage de l'URL de suivi: %s" % str(exception))

#     def notify_tracking_event(self, tracking_result):
#         # Récupérer l'agent utilisateur et l'adresse IP
#         user_agent = tracking_result.request_data.get('HTTP_USER_AGENT', 'Unknown')
#         user_ip = tracking_result.request_data.get('REMOTE_ADDR', 'Unknown')

#         # Envoyer la notification d'ouverture du mail
#         self.send_open_notification(tracking_result.email_id, user_agent, user_ip)

#     def get_configuration(self):
#         # Retourner la configuration pytracking
#         return Configuration()


# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# from django.http import HttpRequest
# from pytracking import Configuration
# from pytracking.django import OpenTrackingView, ClickTrackingView
# from pytracking.webhook import send_webhook
# from pytracking.html import html, adapt_html
# from django.conf import settings
# from cryptography.fernet import Fernet
# import pytracking
# import uuid

# class MyOpenTrackingView(OpenTrackingView):
#     def notify_tracking_event(self, tracking_result):
#         send_webhook(tracking_result)


# class MyClickTrackingView(ClickTrackingView):
#     def notify_tracking_event(self, tracking_result):
#         send_webhook(tracking_result)


# def send_tracked_email(subject, message, recipient_list, html_message=None):
#     # Add tracking pixel to the HTML message
#     html_message_with_tracking = adapt_html(html_message, open_tracking=True, click_tracking=False, extra_metadata={"customer_id": 1})

#     unique_id = uuid.uuid4().hex

#     full_url = f"{settings.PYTRACKING_CONFIGURATION['base_open_tracking_url']}{unique_id}"
    
#     # Send the email
#     send_mail(subject, message, 'serignemourtallasyll86@gmail.com', recipient_list, html_message=html_message_with_tracking)   
#     print(full_url) 
#     # Create a tracking result for the tracking pixel
#     # tracking_result = pytracking.get_open_tracking_result(full_url, base_click_tracking_url=settings.PYTRACKING_CONFIGURATION['base_click_tracking_url'])
#     # # Send webhook notification
#     # send_webhook(tracking_result)

# # Example usage
# subject = "Test Email"
# message = "This is a test email."
# recipient_list = ["serignemourtallasyll972@gmail.com"]
# html_message = "<html><body>This is a test email with a tracking pixel.</body></html>"

# # Send email and track it using a tracking pixel
# send_tracked_email(subject, message, recipient_list, html_message=html_message)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
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

class SendTemplateMailView(APIView):
    def post(self, request, *args, **kwargs):
        target_user_email = request.data.get('email')
        mail_template = get_template("index.html") 
        context_data_is = dict()
        # Construire l'URL de l'image de suivi
        image_url = request.build_absolute_uri(reverse("render_image"))
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

class render_image(APIView):
    def get(self, request):
        if request.method == 'GET':
            current_directory = os.path.dirname(os.path.abspath(__file__))
            image_path = os.path.join(current_directory, 'userAvatar.png')
            
            # Charger l'image à partir du système de fichiers
            image = Image.open(image_path)
            
            # Sauvegarder l'image dans une réponse HTTP
            image_format = image.format if image.format else 'PNG'  # Utilisez le format d'origine si disponible, sinon PNG
            response = HttpResponse(content_type=f"image/{image_format.lower()}")
            image.save(response, image_format)
            
            # Enregistrer l'ouverture de l'e-mail dans la base de données
            email_id = request.query_params.get('email_id')
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