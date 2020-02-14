from django.db import models

class Notification(models.Model):
    MedicineName = models.CharField(max_length=200)
    Hours = models.CharField(max_length=200)
    Minutes = models.CharField(max_length=200)
    Seconds = models.CharField(max_length=200)
    def __str__(self):
        return self.nam


class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    BookChoice = models.CharField(max_length=200)
    Message = models.TextField(blank=True)
    def __str__(self):
     return self.name
