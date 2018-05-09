from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from taxApp.models import Tableinf


class LoginInForm(models.Model):
    IdentNum = models.CharField(max_length=30, verbose_name='识别号')
    password = models.CharField(max_length=50, verbose_name='密码')

class TableinfForm(models.Model):
    taxname = models.CharField(max_length=30, verbose_name='纳税人名称')
    # taxnum = models.CharField(max_length=30, verbose_name='识别号')
    # cancelreason = models.CharField(max_length=30, verbose_name='原因')
    # dataname1 = models.CharField(max_length=30, verbose_name='资料1')
    def clean(self):
        cleaned_data = super(TableinfForm, self).clean()
        value = cleaned_data.get('name')
        try:
            Tableinf.objects.get(name=value)
            self._errors['name']=self.error_class(["%s的信息已经存在" % value])
        except Tableinf.DoesNotExist:
            pass
        return cleaned_data