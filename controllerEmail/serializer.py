from rest_framework import serializers
from .models import EmailTracker

class EmailTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTracker
        fields = ['id', 'recipient_email', 'subject', 'sent_at', 'opened_at']