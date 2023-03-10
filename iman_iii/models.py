from django.db import models


class Numbo_text(models.Model):
    first = models.CharField(max_length=255)
    second = models.CharField(max_length=255)
    third = models.CharField(max_length=255)
    fourth = models.CharField(max_length=255)
    fifth = models.CharField(max_length=255)
