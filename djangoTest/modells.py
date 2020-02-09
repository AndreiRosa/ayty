import django
from django.db import models

class extension(models.Model):
    id_extension = models.BigIntegerField(primary_key=True)
    extension = models.CharField(max_length=4)
    nm_extension = models.CharField(max_length=9)
    is_active = models.BooleanField()
    must_record = models.BooleanField()
    number_transfer = models.CharField(max_length=9, blank=True)
    was_exported = models.BooleanField()

class call(models.Model):
    id_Call = models.BigIntegerField(primary_key=True)
    extension = models.CharField(max_length=4)
    nu_ddd = models.CharField(max_length=2)
    nu_phone = models.CharField(max_length=9)
    dt_start = models.DateTimeField()
    dt_answer = models.DateTimeField()
    dt_finish = models.DateTimeField()
    id_extension = models.ForeignKey(extension, on_delete=models.CASCADE)

class extent_event(models.Model):
    id_extent_event = models.BigIntegerField(primary_key=True)
    extension = models.CharField(max_length=4)
    status = models.CharField(max_length=9)
    dt_event = models.DateTimeField()
    id_extension = models.ForeignKey(extension, on_delete=models.CASCADE)

