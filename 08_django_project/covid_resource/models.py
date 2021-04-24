from django.db import models


class CovidResource(models.Model):
    """
        Covid Resource Model
    """

    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=15)
    contact_website = models.URLField()
    # is_whatsapp_available = models.BooleanField()

    def __str__(self):
        return self.title

