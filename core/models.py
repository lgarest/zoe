from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=60)
    message=models.TextField()

    def __unicode__(self):
        return self.subject + ': ' + self.email