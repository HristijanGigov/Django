from django.db import models

# Create your models here.
class MyData(models.Model):
    text: models.CharField(max_length=100)
    rating: models.IntegerField(max_length=5)
    date: models.IntegerField(max_length=10)
    minRate:models.IntegerField(max_length=5)
    is_true = False #need to click the button to filter the data otherwise it will filter automatically
    