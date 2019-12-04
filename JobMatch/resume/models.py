from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=200, null=True, blank=False)
    top_skills = models.CharField(max_length=200, null=True, blank=True)
    current_job = models.CharField(max_length=200, null=True, blank=True)
    loc = models.CharField(max_length=200, null=True, blank=True)
    languages = models.CharField(max_length=200, null=True, blank=True)
    certs = models.CharField(max_length=200, null=True, blank=True)
    pubs = models.CharField(max_length=200, null=True, blank=True)
    honors = models.CharField(max_length=200, null=True, blank=True)
    summ = models.CharField(max_length=200, null=True, blank=True)
    work_exp = models.CharField(max_length=200, null=True, blank=True)
    edu = models.CharField(max_length=200, null=True, blank=True)
    

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name