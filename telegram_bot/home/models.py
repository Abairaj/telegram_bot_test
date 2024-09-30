from django.db import models

# Create your models here.


class BotData(models.Model):
    user_name = models.CharField(max_length=100)
    json = models.JSONField()
