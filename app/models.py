from django.db import models
from django.db.models.fields import BooleanField, CharField
from django.db.models.deletion import CASCADE
import datetime

class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = 'Username already in use'
        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email is already registered'
        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'
        return errors
    
    def updatePassword(self, form):
        errors = {}
        if form['password'] != form['confirm']:
            errors['password'] = "Passwords do not match"
        return errors

    def updateUsername(self, form):
        errors = {}
        usernameCheck = self.filter(username=form['username'])
        if usernameCheck:
            errors['username'] = 'Username already in use'
        return errors
    
    def updateEmail(self, form):
        errors = {}
        emailCheck = self.filter(email=form['email'])
        if emailCheck:
            errors['email'] = 'Email is already registered'
        return errors


class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=45, unique=True)
    password = models.CharField(max_length=255)
    level = models.IntegerField(default=0)

    objects = UserManager()

    loggedOn = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

