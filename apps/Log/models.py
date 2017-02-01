from __future__ import unicode_literals
import re, bcrypt
from django.db import models
EMAIL_REGEX=re.compile(r'^[a-zA-z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name=re.compile(r'^[a-zA-Z]')


class UserManager(models.Manager):
    def add_user(self, postData):
        errors=[]
        if len(postData['name'])<4:
            errors.append('Name needs more characters.')
        elif not name.match(postData['name']):
            errors.append('No numbers allowed in first name')
        if len(postData['username'])<4:
            errors.append('Please enter a username.')
        if len(postData['password'])<9:
            errors.append('Password needs to be 8 characters or more!')
        if postData['password']!=postData['confirm']:
            errors.append('Password does not match!')


        modelsResponse={}

        if errors:
            modelsResponse['isRegistered'] = False
            modelsResponse ['errors'] = errors
        else:
            modelsResponse['isRegistered'] = True
            hashed_password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user=self.create(name= postData['name'], username=postData['username'],  password=hashed_password)
            modelsResponse['isRegistered'] = True
            modelsResponse['user']= user

        return modelsResponse

    def login_user(self,postData):
        errors=[]
        modelsResponse= {}
        user = self.filter(username = postData['username2'])
        if len(user)<2:
            errors.append('Invalid Username!')
        else:

            if bcrypt.checkpw(postData['password2'].encode(), user[0].password.encode()):
                modelsResponse['isLoggedIn']= True
                modelsResponse['user']= user[0]
            else:
                errors.append('Invalid username/password combination.')
        if errors:
            modelsResponse['isLoggedIn'] = False
            modelsResponse['errors'] = errors

        return modelsResponse


class User(models.Model):
    name=models.CharField(max_length=50)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = UserManager()
