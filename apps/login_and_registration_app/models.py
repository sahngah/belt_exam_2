from __future__ import unicode_literals
import re
import bcrypt
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

class RegisterManager(models.Manager):
    def register(self, data):
        errors = []
        if len(data['first_name']) < 3:
            errors.append('First Name Too Short!')
        elif not NAME_REGEX.match(data['first_name']):
            errors.append('First Name Should Be Letters only!')
        if len(data['last_name']) < 3:
            errors.append('Last Name Too Short!')
        elif not NAME_REGEX.match(data['last_name']):
            errors.append('Last Name Should Be Letters only!')
        if not EMAIL_REGEX.match(data['email']):
            errors.append('Email Should Be In Valid Format!')
        if len(data['password']) < 9:
            errors.append('Password Too Short!')
        elif not data['password'] == data['password_confirmation']:
            errors.append('Passwords Do Not Match!')
        same = User.objects.filter(email = data['email'])
        if same:
            errors.append('Email already in use')

        if errors:
            return {"errors" : errors}
        else:
            hashed = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(first_name = data['first_name'], last_name = data['last_name'], email=data['email'], password=hashed)
# come back when bcrypt!!!!!
            return {'user': user}

    def login(self, data):
        print data
        errors = []
        user = User.objects.filter(email = data['login_email'])
        # userpassword =
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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = RegisterManager()
