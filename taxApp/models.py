from django.db import models



class Zengzhishui(models.Model):
    taxname= models.CharField(max_length=30, verbose_name='法定代表人姓名')
    regadress= models.CharField(max_length=30, verbose_name='注册地址')
    bussadress= models.CharField(max_length=30, verbose_name='生产经营地址')
    def __str__(self):
        return self.taxname
