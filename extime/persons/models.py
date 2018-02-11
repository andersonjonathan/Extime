from django.db import models


class Organisation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Person(models.Model):
    SEX_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    organisation = models.ForeignKey(Organisation, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=63, blank=True, null=True)

    def __str__(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)

    @property
    def name(self):
        return "{first_name} {last_name}".format(first_name=self.first_name, last_name=self.last_name)
