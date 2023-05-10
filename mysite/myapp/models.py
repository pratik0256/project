from django.conf import settings
from django.db import models

class CSVData(models.Model):
    Index = models.IntegerField(default=0)
    M2_Declaration_Number = models.TextField(max_length=2550)
    CIF_Value = models.FloatField()
    Stat_Quantity = models.IntegerField(null=True)
    COMMODITY_DESC = models.TextField(max_length=2500)
    GOODS_DESCRIPTION = models.TextField(max_length=2500)
    unit_price = models.FloatField()
    Test = models.TextField(max_length=2550)
    Test2 = models.TextField(max_length=2550)

    class Meta:
        unique_together = ["Index", "M2_Declaration_Number", "CIF_Value","Stat_Quantity","COMMODITY_DESC","GOODS_DESCRIPTION","unit_price"]
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.user.username    