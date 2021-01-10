from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django.utils import timezone


# Create user and save to the database
#user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# Update fields and then save again
#user.first_name = 'John'
#user.last_name = 'Citizen'
#user.save()

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor  = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


class Prestamo(models.Model):
    libro   = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha   = models.DateField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)