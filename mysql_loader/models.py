from django.db import models



class Names(models.Model):
    name = models.CharField(max_length=10)