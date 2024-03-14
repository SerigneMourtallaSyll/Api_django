# from django.urls import path
# from .views import MyOpenTrackingView

# urlpatterns = [
#     path('', MyOpenTrackingView.as_view(), name="email_tracking"),
#     path('open/<path>/', MyOpenTrackingView.as_view(), name="open_tracking"),
# ]

from django.urls import path , include
from .views import SendTemplateMailView , render_image, GetEmailTrackingData, TrackingPixelView

urlpatterns = [
    path('send/render_image/', render_image.as_view(), name='render_image'),
    path('send/', SendTemplateMailView.as_view(), name='send_template'),
    path('get_image/', GetEmailTrackingData.as_view(), name='get_template'),
    path('tracking/', TrackingPixelView.as_view(), name='tracking_pixel'),
]
