from django.db import models



class Zengzhishui(models.Model):
    taxname= models.CharField(max_length=30, verbose_name='法定代表人姓名')
    regadress= models.CharField(max_length=30, verbose_name='注册地址')
    bussadress= models.CharField(max_length=30, verbose_name='生产经营地址')
    def __str__(self):
        return self.taxname
class Biangen(models.Model):
    taxname = models.CharField(max_length=30, verbose_name='纳税人名称')
    taxnum = models.CharField(max_length=30, verbose_name='识别号')
    def __str__(self):
        return self.taxname

class Tableinf(models.Model):
    taxname = models.CharField(max_length=30, verbose_name='纳税人名称')
    taxnum = models.CharField(max_length=30, verbose_name='识别号')
    # cancelreason = models.CharField(max_length=30, verbose_name='原因')
    # dataname1 = models.CharField(max_length=30, verbose_name='资料1')
    def __str__(self):
        return self.taxname