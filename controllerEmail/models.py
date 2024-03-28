from django.db import models
from django.db.models import Max
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import uuid

def document_upload_path(instance, filename):
    return f'email_documents/{instance.id}/{filename}'

def image_upload_path(instance, filename):
    return f'email_images/{instance.id}/{filename}'

class EmailTracker(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    sent_at = models.DateTimeField(auto_now_add=True)
    opened_at = models.DateTimeField(null=True, blank=True)
    email_id = models.UUIDField(default=uuid.uuid4, editable=False)
    document = models.ManyToManyField('Document', blank=True)
    image = models.ManyToManyField('Images', blank=True)

    def get_last_opened_at(self):
        last_opening = self.emailtracking_set.aggregate(last_opened=Max('opened_at'))['last_opened']
        return last_opening

class Document(models.Model):
    file = models.FileField(upload_to=document_upload_path)

@receiver(pre_delete, sender=Document)
def delete_document_file(sender, instance, **kwargs):
    # Supprimer le fichier de document du stockage lors de la suppression de l'instance Document
    if instance.file:
        if default_storage.exists(instance.file.name):
            default_storage.delete(instance.file.name)

class Images(models.Model):
    file = models.ImageField(upload_to=image_upload_path)

@receiver(pre_delete, sender=Images)
def delete_image_file(sender, instance, **kwargs):
    # Supprimer le fichier d'image du stockage lors de la suppression de l'instance Images
    if instance.file:
        if default_storage.exists(instance.file.name):
            default_storage.delete(instance.file.name)

class EmailTracking(models.Model):
    email = models.ForeignKey(EmailTracker, on_delete=models.CASCADE)
    opened_at = models.DateTimeField(auto_now_add=True, null=True)
