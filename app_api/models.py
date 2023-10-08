import csv
import io
import json

from django.db import models


# Create your models here.
class DataFile(models.Model):
    name = models.CharField(max_length=255, editable=False, null=False, blank=True)
    file = models.FileField(upload_to="files/")
    uploaded_at = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=True)
    columns = models.TextField(editable=False, null=False, blank=True)  # JSON serialized list of columns.

    def save(self, *args, **kwargs):
        if self.file:
            self.name = self.file.name

            file = self.file.read().decode('utf-8')
            csv_data = csv.reader(io.StringIO(file), delimiter=',')

            headers = next(csv_data)  # Get the first row, which should be the headers/column names
            self.columns = json.dumps(headers)

        super().save(*args, **kwargs)

