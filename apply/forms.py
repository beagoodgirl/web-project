from django import forms
from .models import Person
from django.core.exceptions import ValidationError

class PersonModelForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['acc', 'tel', 'amount', 'take_id', 'address'] 

        # widget 用來設定介面的呈現
        widgets = {
            'acc': forms.TextInput(attrs = {'class': 'form-control'}),
            'tel': forms.TextInput(attrs = {'class': 'form-control'}),
            'amount': forms.TextInput(attrs = {'class': 'form-control'}),
            'take_id': forms.RadioSelect(),
            'address': forms.TextInput(attrs = {'class': 'form-control'})
            # 'voucher_id': forms.Select(attrs = {'class': 'form-control'}),
        }

        labels = {
            'acc': '帳號',
            'amount': '訂購數量',
            'tel': '電話號碼',
            'take_id': '領取方式',
            'address':'地址(請必須填寫)'
        }

    # override the clean_<fieldname>() method
    # 帳號必須剛好 10 個字
    def clean_acc(self):
        data = self.cleaned_data['acc'] # 通過基本檢查乾淨資料

        if len(data) != 10 :
            raise ValidationError('帳號長度必須為 10')
        # Remember to always return the cleaned data.
        return data

    # 電話號碼必須等於10個字
    def clean_tel(self):
        data = self.cleaned_data['tel']
        if len(data) != 10 :
            raise ValidationError('電話長度須等於10')

        # Remember to always return the cleaned data.
        return data        
    
    def clean_amount(self):
        data = self.cleaned_data['amount']
        if data > 300:
            raise ValidationError('數量過多，請分批購買')
        if data < 0:
            raise ValidationError('請輸入正確數量')
        
        return data
    
    def clean_address(self):
        data = self.cleaned_data['address']
        if len(data) == 0:
                raise ValidationError('請輸入地址')
        return data