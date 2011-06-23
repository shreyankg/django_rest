from django.db import models
from django.forms import ModelForm

# Create your models here.

class Soap(models.Model):
    name = models.CharField(max_length=200)
    no_of_seasons = models.IntegerField('number of seasons')

class SoapForm(ModelForm):
    class Meta:
        model = Soap
