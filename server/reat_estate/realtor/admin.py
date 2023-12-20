from django.contrib import admin
from .models import Realtor
# Register your models here.

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    
    list_display = ('id','name','email','date_hired','top_seller')
    list_display_links = ('id','name')
    search_fields = ('name','email')
    list_per_page = 10