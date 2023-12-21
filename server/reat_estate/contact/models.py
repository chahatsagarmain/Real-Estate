from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique  = True)
    subject = models.CharField(max_length = 200)
    message = models.TextField(blank = True)
    contact_date = models.DateTimeField(default = datetime.now())
    
    
    def __str__(self):
        return self.name
    
    
