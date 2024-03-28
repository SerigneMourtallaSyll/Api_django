from django.urls import path , include
from .views import SendTemplateMailView , GetEmailTrackingData, tracking_pixel, EmailTrackerDetailView

urlpatterns = [
    path('send/', SendTemplateMailView.as_view(), name='send_template'),
    path('get-email-tracking-data/', GetEmailTrackingData.as_view(), name='get_email_tracking_data'),
    path('tracking/', tracking_pixel.as_view(), name='tracking_pixel'),
    path('email-tracker/<int:pk>/', EmailTrackerDetailView.as_view(), name='email_tracker_detail'),
]
