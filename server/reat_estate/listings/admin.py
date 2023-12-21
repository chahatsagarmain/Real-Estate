from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Listings

# Register your models here.
@admin.register(Listings)
class ListingAdmin(ModelAdmin):
    
    class Meta:
        model = Listings
        list_display = ('id','title','is_published' , 'price' , 'listing_date' , 'realtor')
        list_display_links = ('id','title')
        list_per_page = 10
        list_filter = ('title','realtor')
        list_editable = ('is_published')
        search_fields = ('title','state','city','zipcode','description')
        