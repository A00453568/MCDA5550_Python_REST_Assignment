from django.db import models
# from rest_framework.serializers import (CharField, IntegerField, ListField, FloatField)
# from rest_framework.serializers import Serializer

# Create your models here.

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Hotel'