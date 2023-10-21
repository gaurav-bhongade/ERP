from django.db import models

# Create your models here.

class Stock(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    minqty_required = models.IntegerField()
    maxqty_required = models.IntegerField()
    cost_per_unit = models.FloatField()
    usage_level = models.CharField(
        max_length=30,
        choices=[
            ('Low level', 'Low level'),
            ('Mid level', 'Mid level'),
            ('High level', 'High level'),
        ],
        default='Low level',
    )
    reorder_duration = models.CharField(
        max_length=30,
        choices=[
            ('1 week', '1 week'),
            ('3-4 days', '3-4 days'),
            ('1-2 days', '1-2 days'),
        ],
        default='1 week',
    )
    supplier_id = models.ForeignKey('Supplier', on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = "stock_master"

    def __str__(self):
        return f'''{self.__dict__}'''
    
    def __repr__(self):
        return str(self)

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=150)
    location = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    stock_product_id = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
    stock_name = models.CharField(max_length=100)
    gst_no = models.CharField(max_length=20)
    rating = models.CharField(
        max_length=30,
        choices=[
            ('1 star', '1 star'),
            ('2 star', '2 star'),
            ('3 star', '3 star'),
            ('4 star', '4 star'),
            ('5 star', '5 star'),
        ],
        default='1 star',
    )

    class Meta:
        db_table="supplier_master"

    def __str__(self):
        return f'''{self.__dict__}'''
    
    def __repr__(self):
        return str(self)