from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.base import Model
from datetime import datetime
from .models import *

class createReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['date', 'name', 'phone']

class createRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_type', 'time_slot', 'price', 'status', 'roomnumber']
        
class UserForm(forms.ModelForm):
    user_id = forms.ModelChoiceField(queryset=User.objects.all(),required=False)
    
    class Meta:
        model = User
        fields = ['user_id']