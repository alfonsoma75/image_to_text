from django.db import models


class ImageModel(models.Model):
    image = models.ImageField(upload_to='tmp/')
    unique_id = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.unique_id)

