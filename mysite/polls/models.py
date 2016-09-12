from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from timezone_field import TimeZoneField
from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Appointment #{0} - {1}'.format(self.pk, self.name)

# Create your models here.
