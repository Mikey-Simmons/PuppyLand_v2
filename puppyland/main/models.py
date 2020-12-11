from django.db import models
import re 

class DogManager(models.Manager):
    def dog_validator(self,postData):
        errors = {}
        if len(postData['dog_name']) < 1:
            errors['customer_name'] = "Name must be more than 1 characters!"
        if len(postData['dog_breed']) < 2:
            errors['dog_breed'] = "Description must be more than 2 characters!"
        if len(postData['dog_gender']) < 1:
            errors['dog_gender'] = "Must put gender"
        return errors
class Dog(models.Model):
    dog_name = models.CharField(max_length=255)
    dog_breed = models.CharField(max_length=255)
    dog_gender = models.CharField(default = 000, max_length = 20)
    dog_weight = models.IntegerField()
    dog_age=models.IntegerField()
    img = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= DogManager()
class UserManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors['first_name'] = "First name needs to be at least 3 characters"
        if len(postData['last_name']) < 3:
            errors['last_name'] = "Last name needs to be at least 3 characters"
        if len(postData['email']) < 8:
            errors['email'] = "Email needs to be at least 8 characters"
        if len(postData['password']) < 8:
            errors['password'] = "Password needs to be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['invalid_password'] ="Passwords do not match!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        return errors
    def login_validator(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    
            errors['email'] = "Invalid email address!"
        if len(postData['email']) < 8:
            errors['email'] = "Email needs to be at least 8 characters"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()