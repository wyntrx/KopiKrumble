from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('',views.LoginView.as_view(), name="login_view"),
    path('landing',views.LandingView.as_view(), name="landing_view"),
    path('aboutus',views.AboutUsView.as_view(), name = "aboutus_view"),
    path('add-user',views.AddUserView.as_view(), name="add_new_user"),
    path('add-room',views.AddRoom, name="add_room"),
    path('home',views.home, name = "home"),
    path('about',views.about, name = "about"),
    path('contact',views.contact, name = "contact"),
    path('login',views.login, name = "login"),
    path('reservation/',views.ReservationView, name="reservation_view"),
    path('room',views.RoomView.as_view(), name="room_view"),
    
    
    
]