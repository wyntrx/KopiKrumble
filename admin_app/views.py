from django.shortcuts import redirect, render
from django.views.generic import View
from user_app.models import User
from user_app.models import Reservation
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse


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
            reserve = Reservation.objects.all()
            context = {
                'reserve': reserve,
            }
            return render(request,"admin_side/dashboard.html",context)
        else:
            return redirect("user_app:login_view")
        
    def post(self, request):
        if request.method == 'POST':
            if 'btnDelete' in request.POST:
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
