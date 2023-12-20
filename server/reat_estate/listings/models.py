from django.db import models
from realtor.models import Realtor
from datetime import datetime
# Create your models here.
class Listings(models.Model):
    
    sale_choices = (
        ("FOR_SALE" , "For Sale"),
        ("FOR_RENT" , "For Rent")  
    )
    
    home_choices = (
        ("APARTMENT" , "Apartment"),
        ("CONDO" , "Condo"),
        ("FARMHOUSE" , "Farmhouse")
    )
    
    realtor = models.ForeignKey(Realtor,on_delete=models.CASCADE)
    slug = models.CharField(max_length =200 , unique =True)
    title= models.CharField(max_length = 100)
    address = models.CharField(max_length = 150)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 50)
    zipcode = models.CharField(max_length = 20)
    description = models.TextField(blank = True)
    sale_type = models.CharField(max_length = 50 , choices = sale_choices , default = "FOR_SALE")
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    home_type = models.CharField(max_length = 50 , choices = home_choices, default = "APARTMENT")
    area = models.IntegerField()
    open_house = models.BooleanField(default = False)
    photo_main = models.ImageField(upload_to=f'photos/{datetime.now()}')
    photo_1 = models.ImageField(upload_to=f'photos/{datetime.now()}' , blank=True)
    photo_2 = models.ImageField(upload_to=f'photos/{datetime.now()}' , blank=True)
    photo_3 = models.ImageField(upload_to=f'photos/{datetime.now()}' , blank=True)
    photo_4 = models.ImageField(upload_to=f'photos/{datetime.now()}' , blank=True)
    photo_5 = models.ImageField(upload_to=f'photos/{datetime.now()}' , blank=True)
    photo_6 = models.ImageField(upload_to=f'photos/{datetime.now()}' , blank=True)
    photo_7 = models.ImageField(upload_to=f'photos/{datetime.now()}' , blank=True)
    photo_8 = models.ImageField(upload_to=f'photos/{datetime.now()}' , blank=True)
    photo_9 = models.ImageField(upload_to=f'photos/{datetime.now()}' , blank=True)
    photo_10 = models.ImageField(upload_to=f'photos/{datetime.now()}' , blank = True)
    listing_date = models.DateField(default = datetime.now())
    is_published = models.BooleanField(default = True)
    
    def __str__(self):
        return self.title 
    
    
    
    
    
    
    
    