from django import forms
from .models import Profile,Neighborhood
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'bio']

class NeighborhoodForm(forms.ModelForm):
    
    class Meta:
        model = Neighborhood
        fields = [ 'name','location','police','police_department_address','health','health_department_address']
