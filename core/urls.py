from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('franchise-dashboard/', views.franchise_dashboard, name='franchise_dashboard'),
    path('lead-dashboard/', views.lead_dashboard, name='lead_dashboard'),
    path('marketing-dashboard/', views.marketing_dashboard, name='marketing_dashboard'),
    path('admin-logout/', views.admin_logout, name='admin_logout'),
    path('products/', views.products, name='products'),
    path('coupons/', views.coupons, name='coupons'),
    path('add-franchise/', views.add_franchise, name='add_franchise'),
    path('add-coupon/', views.add_coupon, name='add_coupon'),
    path('add-marketing-member/', views.add_marketing_member, name='add_marketing_member'),
    path('user-login/', views.user_login, name='user_login'),
    path('user-signup/', views.user_signup, name='user_signup'),
    path('send-signup-otp/', views.send_signup_otp, name='send_signup_otp'),
]
