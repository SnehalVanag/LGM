from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('manager-dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('franchise-dashboard/', views.franchise_dashboard, name='franchise_dashboard'),
    path('lead-dashboard/', views.lead_dashboard, name='lead_dashboard'),
    path('marketing-dashboard/', views.marketing_dashboard, name='marketing_dashboard'),
    path('', include('core.urls')),
]
