from django import forms

class ImageForm(forms.Form):
    dog_name = forms.CharField(max_length=255)
    dog_name = forms.CharField(max_length=255)
    dog_breed = forms.CharField(max_length=255)
    dog_gender = forms.CharField(max_length = 20)
    dog_weight = forms.IntegerField()
    dog_age= forms.CharField(max_length=200)
    dog_price = forms.IntegerField()
    img = forms.FileField()
    