from django.db import models


# Create your models here.
class DataFile(models.Model):
    name = models.CharField(max_length=255, editable=False, null=False, blank=True)
    file = models.FileField(upload_to="files/")
    uploaded_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=True)
    columns = models.TextField(editable=False, null=False, blank=True)  # JSON serialized list of columns.
