from django.db import models

"""
ll db.sqlite3 __pycache__ ; find lists/migrations -ls

manage.py test
django.db.utils.OperationalError: no such column: lists_item.text
manage.py makemigrations
manage.py migrate

"""

class List(models.Model):
    text = models.TextField(default='')


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

