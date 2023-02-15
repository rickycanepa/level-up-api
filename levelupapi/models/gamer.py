from django.db import models
from django.contrib.auth.models import User

class Gamer(models.Model):

    # One to one relationship with the User model, includes name & email
    user = models.OneToOneField("Gamer", on_delete=models.CASCADE)
    # bio field from client
    bio = models.CharField

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'