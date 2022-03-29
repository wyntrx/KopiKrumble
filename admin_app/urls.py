from django.urls import path
from . import views
app_name = 'admin_app'

urlpatterns = [
    
    #path('index',views.index2, name = "index2"),
    path('dashboard',views.Dashboard.as_view(), name='dashboard'),
    path('admin-view',views.AdminView.as_view(), name="admin_view"),
    path('list-view',views.ListView.as_view(), name='list_view'),
]