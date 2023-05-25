from django.db import models


class Users(models.Model):
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        ordering = ['email']

    def __str__(self):
        return f'{self.email, self.password}'

