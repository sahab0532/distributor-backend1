from django.db import models

class Distributor(models.Model):
    name = models.CharField(max_length=255)
    gst_number = models.CharField(max_length=15, unique=True)
    pan_number = models.CharField(max_length=10, unique=True)
    bank_account = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=11)
    address = models.TextField()

class Payment(models.Model):
    STATUS_CHOICES = [('PENDING', 'Pending'), ('SUCCESS', 'Success'), ('FAILED', 'Failed')]
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    metadata = models.JSONField(default=dict)
