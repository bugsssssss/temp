from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(("title"), max_length=255)
    text = models.TextField(("text"), blank=True, null=True)
    image = models.ImageField(("image"), upload_to='images', height_field=None, width_field=None, max_length=None)
    created = models.DateTimeField(("created"), auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['-created']