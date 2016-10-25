from __future__ import unicode_literals
import re
import bcrypt
from django.db import models
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class RegisterManager(models.Manager):
    def register(self, data):
        errors = []
        if len(data['name']) < 3:
            errors.append('Name Too Short (should contain at least 3 characters)!')
        elif not NAME_REGEX.match(data['name']):
            errors.append('Name Should Be Letters only!')
        if len(data['username']) < 3:
            errors.append('Username Too Short (should contain at least 3 characters)!')
        if len(data['password']) < 9:
            errors.append('Password Too Short!')
        elif not data['password'] == data['password_confirmation']:
            errors.append('Passwords Do Not Match!')
        same = User.objects.filter(username = data['username'])
        if same:
            errors.append('Username already in use')

        if errors:
            return {"errors" : errors}
        else:
            hashed = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(name = data['name'], username=data['username'], password=hashed, date_hired=data['date_hired'])
# come back when bcrypt!!!!!
            return {'user': user}

    def login(self, data):
        print data
        errors = []
        user = User.objects.filter(username = data['login_username'])
        if user:
            if user[0].password == bcrypt.hashpw(data['login_password'].encode(), user[0].password.encode()):
                return {'user' : user[0]}
        else:
            return {'errors' : "Failed to login: try again!"}
        #     errors.append('User email does not exist!')
        # if not data['password'] == userlist['password']:
        #     errors.append('User password does not match!')
        #


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=60)
    password = models.CharField(max_length=1000)
    date_hired = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = RegisterManager()
