from django.db import models

class Skills(models.Model):
    skills = models.TextField()
    
    
class DataSkill(models.Model):
    dataskill = models.CharField(max_length=255, blank=True)
    area = models.CharField(max_length=255, blank=True)
    percentage = models.FloatField()
    
    def __str__(self):
        return self.dataskill