from django.db import models

# Create your models here.
class Contact (models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    info = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=(
        ('male','Male'),
        ('female','Female')
    ))
    image = models.ImageField(upload_to='images/',blank=True)
    date_added  = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    