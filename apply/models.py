from django.db import models
from django.contrib.auth.models import User     # new

# Create your models here.
class Person(models.Model):

    VOUCHER_CHOICES = [
        ('PE', '自取'),
        ('SE', '郵寄'),
    ]
    ssn = models.CharField(max_length=10, blank=False)
    # amount = models.CharField(max_length=3, blank=False)
    tel = models.CharField(max_length=20, blank=False)
    voucher_id = models.CharField(max_length=2, choices = VOUCHER_CHOICES, default='PP')
    account = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) # new

    class Meta:
        ordering = ['-ssn']

    def __str__(self):
        return self.ssn + ", " + str(self.account)
