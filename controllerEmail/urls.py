# from django.urls import path
# from .views import MyOpenTrackingView

# urlpatterns = [
#     path('', MyOpenTrackingView.as_view(), name="email_tracking"),
#     path('open/<path>/', MyOpenTrackingView.as_view(), name="open_tracking"),
# ]

from django.urls import path , include
from .views import SendTemplateMailView , GetEmailTrackingData, tracking_pixel, GetZone

urlpatterns = [
    path('send/', SendTemplateMailView.as_view(), name='send_template'),
    path('get_image/', GetEmailTrackingData.as_view(), name='get_template'),
    path('tracking/', tracking_pixel.as_view(), name='tracking_pixel'),
    path('getZone/', GetZone.as_view(), name='GetZone'),
    
]
