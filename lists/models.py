from django.db import models

# Create your models here.

# manage.py test
# django.db.utils.OperationalError: no such column: lists_item.text
# manage.py makemigrations

class Item(models.Model):
    text = models.TextField(default='')
