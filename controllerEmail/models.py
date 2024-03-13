# from django.db import models

# class TrackingData(models.Model):
#     user_id = models.CharField(max_length=100)
#     email_id = models.CharField(max_length=100)
#     ip_address = models.CharField(max_length=100)
#     user_agent = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     open_timestamp = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return f"Tracking Data: {self.user_id}, {self.email_id}, {self.timestamp}, {self.open_timestamp}, {self.ip_address}, {self.user_agent}"

# from django.db import models

# class Email(models.Model):
#     subject = models.CharField(max_length=255)
#     body = models.TextField()
#     sender = models.EmailField()
#     recipient = models.EmailField()
#     sent_at = models.DateTimeField(auto_now_add=True)
#     opened = models.BooleanField(default=False) 
#     opened_at = models.DateTimeField(null=True, blank=True) 

#     def mark_as_opened(self):
#         self.opened = True
#         self.opened_at = timezone.now()
#         self.save()

from django.db import models
from django.db.models.fields import CharField, EmailField, UUIDField
# Create your models here.
class EmailTracker(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    sent_at = models.DateTimeField(auto_now_add=True)
    opened_at = models.DateTimeField(null=True, blank=True)

class EmailTracking(models.Model):
    email = models.ForeignKey(EmailTracker, on_delete=models.CASCADE)
    opened_at = models.DateTimeField(auto_now_add=True)
