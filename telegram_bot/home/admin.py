from django.contrib import admin
from .models import BotData

# Register your models here.


@admin.register(BotData)
class BotDataAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'json')
