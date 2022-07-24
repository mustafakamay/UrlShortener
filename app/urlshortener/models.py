from django.db import models

class UrlShortener(models.Model):
    originUrl = models.CharField(max_length=250,unique=True)
    shortUrl = models.CharField(max_length=15, blank=True, null=True,unique=True)
    visit = models.IntegerField(default=0)
    
    def __str__(self):
        return self.shortUrl
