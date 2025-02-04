from django.contrib import admin
from .models import AttastModel
# Register your models here.
class AdminPanel(admin.ModelAdmin):
    list_display = ['ism', 'tell', 'ruyxatdanUtishVaqti'] 
    

admin.site.register(AttastModel, AdminPanel)