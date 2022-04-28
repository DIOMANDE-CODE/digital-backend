from django.contrib import admin
from .models import Emailing
# Register your models here.

class EmailingAdmin(admin.ModelAdmin):
    list_display = ('nom', 'mail', 'sujet', 'message')

admin.site.register(Emailing, EmailingAdmin)
