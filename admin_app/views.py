from django.shortcuts import redirect, render
from django.views.generic import View
from user_app.models import User
from user_app.models import Reservation
from django.urls import reverse
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from datetime import date, timedelta, datetime


# Create your views here.
class AdminView(View): 
    def get(self, request):
        if request.user.is_staff:
            users = User.objects.all()
            context = {
                'users': users,
            }
            return render(request,"admin_side/alluser.html",context)
        else:
            return redirect("user_app:login_view")

    def post(self, request):
        if request.method == 'POST':
            if 'btnDelete' in request.POST:
                print("deleted")
                cid = request.POST.get("user-id")
                cust = User.objects.filter(id = cid).delete()
                print('deleted')
                return redirect("admin_app:list_view")
        
            elif 'btnUpdate' in request.POST:
                user_id = request.POST.get("u-id")
                username = request.POST.get("username")
                firstname = request.POST.get("u-fname")
                lastname = request.POST.get("customer-lname")
                email = request.POST.get("customer-address")
                    
                update_user = User.objects.filter(id = user_id).update(username = username, first_name = firstname, last_name = lastname ,email=email)
                return redirect('admin_app:list_view')

#def index2(request):
#    if not request.user.is_staff:
#        users = User.objects.all()
#        context = {
#            'users': users,
#        }
#        return render(request,"admin_side/alluser.html",context)
#    else:
#        return redirect("user_app:login_view")

class ListView(View):
    def get(self, request):
        if not request.user.is_staff:
            users = User.objects.all()
            context = {
                'users': users,
            }
            return render(request,"admin_side/alluser.html",context)
        else:
            return redirect("user_app:login_view")

    def post(self, request):
        if request.method == 'POST':
            if 'btnDelete' in request.POST:
                print("deleted")
                cid = request.POST.get("user-id")
                cust = User.objects.filter(id = cid).delete()
                print('deleted')
                return redirect("admin_app:list_view")
        
            elif 'btnUpdate' in request.POST:
                user_id = request.POST.get("u-id")
                username = request.POST.get("username")
                firstname = request.POST.get("u-fname")
                lastname = request.POST.get("customer-lname")
                email = request.POST.get("customer-address")
                    
                update_user = User.objects.filter(id = user_id).update(username = username, first_name = firstname, last_name = lastname ,email=email)
                return redirect('admin_app:list_view')

class Dashboard(View):
    def get(self, request):
        if request.user.is_staff:
            #get counts
            count_RoomA = Reservation.objects.filter(room = 1).count() #--> to be tested
            count_RoomB = Reservation.objects.filter(room = 2).count()
            count_RoomC = Reservation.objects.filter(room = 3).count()
            count_RoomD = Reservation.objects.filter(room = 4).count()
            #get counts Months
            start_date = datetime.today()
            mend_date = start_date + timedelta(days = 31)
            #get counts Weeks
            wend_date = start_date + timedelta(days = 7)
            #get list & filter search
            count_months = Reservation.objects.filter(date__range = [start_date, mend_date]).count()
            count_weeks = Reservation.objects.filter(date__range = [start_date, wend_date]).count()
            count_today = Reservation.objects.filter(date = start_date).count()
            reserve = Reservation.objects.all().order_by('date')

            context = {
            #List
            'reserve': reserve,
            #count_room context
            'count_RoomA': count_RoomA, #--> to be tested
            'count_RoomB': count_RoomB,
            'count_RoomC': count_RoomC,
            'count_RoomD': count_RoomD,
            #count_Months\Days\Weeks T_T
            'count_months' : count_months, #--> to be tested
            'count_weeks' : count_weeks,
            'count_today' : count_today,
            }
            return render(request,"admin_side/dashboard.html",context)
        else:
            return redirect("user_app:login_view")
        
    def post(self, request):
        if request.method == 'POST' :
            if 'search_res' in request.POST:
                search_res = request.POST.get('search_res')
                reserve = Reservation.objects.filter(reservation_icontains = search_res).order_by('date') #-->to be tested
                if len(reserve) == 0:
                    messages.warning(request, "Please, Try Again!")
                context = {
                'reserve': reserve,
                }
                return render(request,"admin_side/dashboard.html", context)

            elif 'btnDelete' in request.POST:
                print("deleted")
                cid = request.POST.get("reservation-id")
                cust = Reservation.objects.filter(id = cid).delete()
                print('deleted')
                return redirect("admin_app:dashboard")
        
            elif 'btnUpdate' in request.POST:
                rid = request.POST.get("reservation_id")
                rnm = request.POST.get("name")
                rphn = request.POST.get("phone")
                rrm = request.POST.get("room_id")
                    
                update_reservation = Reservation.objects.filter(reservation_id = rid).update(name = rnm, phone = rphn , room = rrm)
                return redirect('admin_app:dashboard')
    
    

def dashboard(request):
    return render(request, 'admin_side/dashboard.html')
