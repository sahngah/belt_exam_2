from __future__ import unicode_literals
from ..login_and_registration_app.models import User
from django.db import models

# Create your models here.
class ItemManager(models.Manager):
    def additem(self, data, user):
        errors=[]
        if len(data['item']) < 4:
            errors.append('Should be more than 3 characters!')
        if errors:
            return {'errors': errors}
        else:
            item = Item.objects.create(user = user, item = data['item'])
            return {'item': item}

class Item(models.Model):
    item = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ItemManager()
    users = models.ManyToManyField(User, related_name = "items_added")
    user = models.ForeignKey(User, related_name = "item_created")
