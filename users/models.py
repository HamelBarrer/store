from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
