from django.db import models
from datetime import datetime
# Create your models here.

class Realtor(models.Model):
    
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=f"photos/{datetime.now()}")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now())
    
    
    def __str__(self):
        return self.name