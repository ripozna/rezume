from rezume import forms
from django import forms
from django.db.models import fields
from rezume.models import Info

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Info
#         fields = '__all__'
        
class RegistrationForm(forms.Form):
    image =forms.ImageField()
    name= forms.CharField(max_length=1000)
    surname= forms.CharField(max_length=1000)
    phone_number = forms.CharField(max_length=1000)
    date_of_birth = forms.CharField(max_length=1000)
    purpose= forms.CharField(max_length=1000)
    education= forms.CharField(max_length=1000)
    professional_skills= forms.CharField(max_length=1000)
    personal_qualities= forms.CharField(max_length=1000)
    additional_information= forms.CharField(max_length=1000)
    
# class RegistrationForm(forms.ModelForm):  
#     class Meta:
#         model = Info
#         fields = ('image',' name','surname','phone_number','date_of_birth','purpose','education','personal_qualities','additional_information')

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Info
#         fields = '__all__'
        