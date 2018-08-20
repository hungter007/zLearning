# _*_ coding: utf-8 _*_
from django import forms
from operation.models import UserAsk
import re


class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):  # clean_  + fields 变量名
        mobile = self.cleaned_data['mobile']  # cleaned_data为内置变量 字典类型
        REGEX_MOBILE = "^1[138]\d{8}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalue")  # 抛出异常