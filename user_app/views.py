
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group, User #, auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import *
from .forms import *
# from .models import CustomUser
from django.contrib.auth.decorators import login_required

from django.http import Http404
import os


# Create your views here.
# class LandingView(View):
#     def post(self, request):
#         if request.method == 'POST':
#             print(request.POST)
#             date = request.POST.get("date")
#             time = request.POST.get("time_slot")
#             roomtype = request.POST.get("room_type")

#             room = Room.objects.filter(status=1,time_slot=time, room_type=roomtype)
#             if len(room) == 0:
#                 messages.warning(request, "Sorry, No rooms are available on this time period.")
            
#             context = {
#                 'room' : room,
#             }
#             return render(request, 'user/index.html', context)
#         else:
#             return redirect('user_app:landing_view')


def ReservationView(request):
    if request.method == 'POST':
        form = createReservationForm(request.POST)
        if form.is_valid():
            form.save()
            customer_name = form.cleaned_data.get('name')
            messages.success(request, f'{customer_name} successfully reserved a room.')
            return redirect('user_app:reservation_view')
    else:
        form = createReservationForm
    context = {
        'form': form
    }
    return render(request, 'user/reservation.html', context)
    

class LoginView(View):
    def get(self,request):
        if not request.user.is_authenticated:
            return render(request, 'user/signin.html')
        else:
            if not request.user.is_staff:
                return redirect("user_app:landing_view")
            else:
                return redirect("admin_app:dashboard")
                          
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            # print("hello")
            #login(request, user)
            if not request.user.is_staff:
                return redirect("user_app:landing_view")
            else:
                return redirect("admin_app:dashboard") #user_dashboard_view
        else:
            # print("incorrect")
            return redirect('user_app:login_view')
            # return HttpResponse("Incorrect!")
                




class AboutUsView(View): 
    def get(self, request):
        return render(request, 'user/aboutus.html') #, context

class AddUserView(View): 
    def get(self, request):
        return render(request, 'user/adduser.html') #, context
    def post(self,request):
        # return render(request, 'Registration_page.html', context)
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = request.user
        User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        # form = UserForm(request.POST)
        # if form.is_valid():
        #     custom_user = form.save(commit=False)
        #     custom_user.user_id = user
        #     custom_user.save()     
        return redirect('user_app:login_view')
        # else:
        #     return HttpResponse(form.errors)

def AddRoom(request):
    submitted = False
    if request.method == "POST":

        form = createRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_app:room_view')
    else:
        form = createRoomForm
    return render(request, 'user/add_room.html',{'form': form})
#     room = Room.objects.all()
#     if request.method == "POST":
#         form = createRoom(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('user_app:add_room')
    # else:
    #     form = createRoom
    # return render(request, 'user/room.html',{'form': form})


class LandingView(View):
    def get(self, request):
        return render(request, 'user/index.html')
    def post(self, request):
        if request.method == 'POST':
            print(request.POST)
            date = request.POST.get("date")
            time = request.POST.get("time_slot")
            roomtype = request.POST.get("room_type")

            room = Room.objects.filter(status=1,time_slot=time, room_type=roomtype)
            if len(room) == 0:
                messages.warning(request, "Sorry, No rooms are available on this time period.")
            
            context = {
                'room' : room,
            }
            return render(request, 'user/index.html', context)
        else:
            return redirect('user_app:landing_view')

class RoomView(View):
    def get(self, request):
        room = Room.objects.all()
        reservation = Reservation.objects.all()
        context = {
            'room' : room,
            'reservation' : reservation,
        }
        return render(request, 'user/room.html', context)




def home(request):
    return render(request, "user/index.html")
def about(request):
    return render(request, "user/aboutus.html")
def contact(request):
    return render(request, "user/contactus.html")
def login(request):
    return render(request, "user/signin.html")
# def landing(request):
#     return render(request, "user/landing.html")
