from django.db import models
from datetime import datetime
from django.utils import timezone
from user_app.utils import create_new_ref_number
import uuid 
from django.contrib.auth.models import User
# Create your models here.


class Person(models.Model):
    userid = models.AutoField(primary_key= True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    bdate = models.DateField(default=timezone.now)
    email = models.EmailField()
    gender = models.CharField(max_length=50)
    address = models.TextField(max_length=191)
    usertype = models.CharField(max_length=50, null= True)
    def __str__(self):
        return self.fname + ' ' + self.lname
    class Meta:
        db_table = 'Person'


class Room(models.Model):
    ROOM_STATUS = ( 
    ("0", "Not available"), 
    ("1", "Available"),    
    ) 

    ROOM_TYPE = ( 
    ("A", "A"), 
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),     
    )

    TIME_SLOT = (
        ("M", "Morning (9:00 to 12:00)"),
        ("A", "Afternoon (13:00 to 17:00)"),
        ("E", "Evening (18:00 to 22:00"),
    ) 

    
    room_type = models.CharField(max_length=50,choices = ROOM_TYPE)
    time_slot = models.CharField(max_length=100,choices = TIME_SLOT)
    price = models.IntegerField()
    status = models.CharField(choices =ROOM_STATUS,max_length = 15)
    roomnumber = models.IntegerField()
    def __str__(self):
        return str(self.roomnumber)
    class Meta:
        db_table = 'Room'
    
class Reservation(models.Model):
    date = models.DateField(auto_now =False)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    reservation_id = models.AutoField(primary_key= True, unique=True, editable=False)
    # reservation_id = models.CharField(
    #     max_length = 10,
    #     blank=True,
    #     editable=False,
    #     unique=True,
    #     default=create_new_ref_number()
    #   )
    def __str__(self):
        return str(self.reservation_id)
    class Meta:
        db_table = 'Reservation'
