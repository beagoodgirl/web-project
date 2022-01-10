from abc import abstractstaticmethod
from django.db import models
from django.db.models import IntegerField
from django.contrib.auth.models import User     # new

# Create your models here.
class Person(models.Model):

    VOUCHER_CHOICES = [
        ('PE', '自取'),
        ('SE', '郵寄'),
    ] 
    acc = models.CharField(max_length=10, blank=False,default='')
    amount = models.IntegerField( blank=False,default='')
    tel = models.CharField(max_length=10, blank=False,default='')
    take_id = models.CharField(max_length=2, choices = VOUCHER_CHOICES, default='PE')
    address = models.CharField(max_length=25, blank=False,default='')
    account = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # new

    class Meta:
        ordering = ['-acc']

    def __str__(self):
        return self.acc + ", " + str(self.take_id)
