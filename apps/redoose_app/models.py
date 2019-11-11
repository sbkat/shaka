from django.db import models

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        user_from_db = User.objects.filter(email=postData['email'])
        if len(user_from_db) != 0:
            if postData['email'] == user_from_db[0].email:
                errors['email'] = "Email is already in database."
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be more than 1 character."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be more than 1 character."
        if len(postData['email']) < 5:
                errors['email'] = "Please enter a valid email address."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()