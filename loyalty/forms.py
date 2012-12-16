__author__ = 'pavelmeshkoy'
from django.contrib.auth.models import User

from django import forms

from loyalty.models import LoyaltyProfile

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = LoyaltyProfile

    def save(self, commit=True):
        user = User()
        try:
            user.username = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.set_password(self.cleaned_data['password'])
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.save()
        except:
            raise Exception("Some Error in the form")




