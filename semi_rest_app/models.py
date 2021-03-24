from django.db import models

class ShowManager(models.Manager):
    def validator(self, form_data):
        errors = {}
        if len(form_data['title']) < 2:
            errors['title'] = 'Show title should at least 2 characters'
        if len(form_data['network']) < 3:
            errors['network'] = 'Show network must be at least 3 characters'
        if len(form_data['desc']) > 0 and len(form_data['desc']) < 10 :
            errors['desc'] = 'Show description must be at least 10 character'
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()