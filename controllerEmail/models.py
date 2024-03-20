from django.db import models
from django.db.models import Max
import uuid

class EmailTracker(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    sent_at = models.DateTimeField(auto_now_add=True)
    opened_at = models.DateTimeField(null=True, blank=True)
    email_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def get_last_opened_at(self):
        last_opening = self.emailtracking_set.aggregate(last_opened=Max('opened_at'))['last_opened']
        return last_opening


class EmailTracking(models.Model):
    email = models.ForeignKey(EmailTracker, on_delete=models.CASCADE)
    opened_at = models.DateTimeField(auto_now_add=True, null=True)
