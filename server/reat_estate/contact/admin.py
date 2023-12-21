from django.contrib import admin
from .models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Contact
        list_display = '__all__'
        list_display_links = ('name')
        search_fields = ('name','email','subject')
        list_per_page = 10
        list_filter = ('name')
        