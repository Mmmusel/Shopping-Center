from django import forms

# 表单类用以生成表单
class AddForm(forms.Form):
    name = forms.CharField()
    brand = forms.CharField()
    cost = forms.FloatField()
    sale = forms.IntegerField()
    img = forms.FileField()