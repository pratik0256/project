from django.conf import settings
from django.db import models

class CSVData(models.Model):
    Index = models.IntegerField(default=0)
    M2_Declaration_Number = models.CharField(max_length=255)
    CIF_Value = models.FloatField()
    Stat_Quantity = models.FloatField()
    COMMODITY_DESC = models.CharField(max_length=255)
    GOODS_DESCRIPTION = models.CharField(max_length=255)
    unit_price = models.FloatField()
    Test = models.CharField(max_length=255)
    Test2 = models.CharField(max_length=255)

    def __str__(self):
        return f"Value :- {self.Index}"
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.user.username    