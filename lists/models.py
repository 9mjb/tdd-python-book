from django.db import models

"""
manage.py test
django.db.utils.OperationalError: no such column: lists_item.text
manage.py makemigrations
manage.py migrate
"""


class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

