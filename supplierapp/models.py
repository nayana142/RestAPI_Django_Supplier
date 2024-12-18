from django.db import models

# Create your models here.
class SupplierDetails(models.Model):
    SUPPLIER_TYPE_CHOICES = [
        ('ST', 'Stockist'),
        ('MF', 'Manufacturer'),
        ('DS', 'Distributor'),
    ]
    profile=models.ImageField(upload_to='supplierimages')
    supplier_name=models.CharField( max_length=50)
    company_name=models.CharField(max_length=50)
    supplier_type=models.CharField(choices=SUPPLIER_TYPE_CHOICES,default='ST',max_length=2)
    category=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    



