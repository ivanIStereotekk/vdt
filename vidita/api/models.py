
from django.db import models
from django.db.models import ForeignKey,CharField,ImageField,SET_NULL,DateField
from datetime import datetime
from django.contrib.auth.models import AbstractUser
import pathlib
from django.conf import settings


class User_Model(AbstractUser):
    """Person who is registred user on django site"""
    on_pictures = models.ForeignKey(
        "Picture_Model", models.SET_NULL, blank=True, null=True, related_name="tagged_on_pictures")

    def __str__(self) -> str:
        return f"{self.username}"

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        ordering = ['username']


class Picture_Model(models.Model):
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True, db_index=True)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True)
    tagged_people = models.ManyToManyField(
        "User_Model", related_name="persons")
    image = models.ImageField(upload_to='uploaded_images/')

    def __str__(self) -> str:
        return f"description: {self.description} uploaded_by: {self.uploaded_by}"

    class Meta:
        verbose_name = 'Picture'
        verbose_name_plural = 'Pictures'
        ordering = ['-date']



        