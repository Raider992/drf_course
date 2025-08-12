from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)

    # AbstractUser._meta.get_field('first_name').verbose_name = 'Имя'
    # AbstractUser._meta.get_field('last_name').verbose_name = 'Фамилия'


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж')                                                                                                   # sometimes camel
    )

    user = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    aboutMe = models.TextField(verbose_name='о себе', max_length=512, blank=True)

    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)