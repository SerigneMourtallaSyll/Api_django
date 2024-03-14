from django.urls import path , include
from .views import SendTemplateMailView , GetEmailTrackingData, tracking_pixel

urlpatterns = [
    path('send/', SendTemplateMailView.as_view(), name='send_template'),
    path('get_image/', GetEmailTrackingData.as_view(), name='get_template'),
    path('tracking/', tracking_pixel.as_view(), name='tracking_pixel'),
]
