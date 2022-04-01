from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.base import Model
from datetime import datetime
from .models import *

class createReservationForm(forms.ModelForm):
    room = forms.ModelChoiceField(queryset=Room.objects.filter(status=1))
    date = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Name'})) 
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))                              
    class Meta:
        model = Reservation
        fields = ['room', 'date', 'name', 'phone' ]

class createRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'time_slot', 'price', 'status', 'roomnumber']
        
class UserForm(forms.ModelForm):
    user_id = forms.ModelChoiceField(queryset=User.objects.all(),required=False)
    
    class Meta:
        model = User
        fields = ['user_id']