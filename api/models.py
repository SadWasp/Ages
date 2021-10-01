from django.db import models

class Item(models.Model):
    name = models.TextField()
    location = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['quantity']

class User(models.Model):
    userName = models.TextField()
    password = models.TextField()

    role = models.TextField()
    nbOrdersFilled = models.IntegerField()
    isConnected = models.BooleanField()

    def __str__(self):
        return self.userName

    class Meta:
        ordering = ['role']