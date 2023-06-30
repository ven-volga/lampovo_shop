from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.email} - {self.name}'
