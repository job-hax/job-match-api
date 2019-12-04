from django.db import models

# Create your models here.
class Stage(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    applied = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    onsite = models.CharField(max_length=200, null=True, blank=True)
    offer = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    

    class Meta:
        ordering = ['applied']

    def __str__(self):
        return self.name