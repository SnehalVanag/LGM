from django.contrib import admin
from django.urls import path,include
from core import views
from .views import add_product

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', admin.site.urls, name='admin'),
    path('login/admin/', views.admin_login, name='admin_login'),
    # path('admin-login/', include(('core.urls', 'core'), namespace='core_admin')),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('', views.home, name='home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
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
    # path('send-signup-otp/', views.send_signup_otp, name='send_signup_otp'),
    path('send-signup-otp/', views.send_signup_otp, name='send_signup_otp'),
    path('marketing-login/', views.marketing_login, name='marketing_login'),
    path('franchise-login/', views.franchise_login, name='franchise_login'),
    path('add_product/', add_product, name='add_product'),
    path('update_product/<int:pk>/', views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('dashboard/', views.dashboard, name='dashboard'),

]
