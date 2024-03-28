from django.db import models

class url(models.Model):
    original_url = models.URLField(max_length=100)
    short_url = models.TextField(max_length=15)
    

