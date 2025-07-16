from django.contrib import admin
from django.urls import path,include
from core import views
from .views import add_product
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/admin/', views.admin_login, name='admin_login'),
    # path('admin-login/', include(('core.urls', 'core'), namespace='core_admin')),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('', views.home, name='home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
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
    path('send-signup-otp/', views.send_signup_otp, name='send_signup_otp'),
    path('marketing-login/', views.marketing_login, name='marketing_login'),
    path('franchise-login/', views.franchise_login, name='franchise_login'),
    path('update_product/<int:pk>/', views.update_product, name='update_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('marketing-dashboard/', views.marketing_dashboard, name='marketing_dashboard'),
    path('coupons/', views.coupon_list, name='coupon_list'),
    path('add-branch/', views.add_branch, name='add_branch'),
    path('delete-branch/<int:branch_id>/', views.delete_branch, name='delete_branch'),
    path('products/', views.products, name='products'),
    path('add-product/', views.add_product, name='add_product'),
    path('delete-franchise/<int:id>/', views.delete_franchise, name='delete_franchise'),
    path('staff/add/', views.add_staff, name='add_staff'),
    path('staff/<int:pk>/edit/', views.edit_staff, name='edit_staff'),
    path('staff/<int:pk>/delete/', views.delete_staff, name='delete_staff'),
    path('franchise-dashboard/', views.franchise_dashboard, name='franchise_dashboard'),
     path('franchise-dashboard/', views.franchise_dashboard, name='franchise_dashboard'),
    # path('admin-login/', views.admin_login, name='admin_login'),
    path('products/', views.products_view, name='products'),
    path('franchise/<int:pk>/edit/', views.edit_franchise, name='edit_franchise'),
    path('franchise/<int:pk>/delete/', views.delete_franchise, name='delete_franchise'),
    path('add-staff/', views.add_staff, name='add_staff'),
    path('signup/', views.user_signup, name='user_signup'),
    path('add-lead/', views.add_lead, name='add_lead'),
     path('send-otp/', views.send_otp, name='send_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('update-coupon/<str:id>/', views.update_coupon, name='update_coupon'),
    path('delete-coupon/<str:id>/', views.delete_coupon, name='delete_coupon'),
    path('edit-franchise/<int:pk>/', views.edit_franchise, name='edit_franchise'),
    path('delete-franchise/<int:pk>/', views.delete_franchise, name='delete_franchise'),
    path('edit-staff/<int:pk>/', views.edit_staff, name='edit_staff'),
    path('delete-staff/<int:pk>/', views.delete_staff, name='delete_staff'),
    path('update-franchise/<int:id>/', views.update_franchise, name='update_franchise'),
    path('toggle-product-status/<int:id>/', views.toggle_product_status, name='toggle_product_status')




  ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    


    # path('coupons/', views.coupon_list, name='coupon_list'),  # <-- This is the important one!  # <-- This is required!


