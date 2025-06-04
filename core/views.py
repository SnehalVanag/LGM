from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime, timedelta
import random, string
from .forms import FranchiseForm
from .models import Franchise
from .models import Coupon
from django.utils import timezone
from .models import Admin
from django.contrib.auth.hashers import check_password 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import MarketingTeamMember, Review
from django.db.models import Avg
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
import random
from django.conf import settings
from .models import AppUser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def home(request):
    return render(request, 'dashboard/home.html')


def manager_dashboard(request):
    return render(request, 'dashboard/home.html')


# def admin_login(request):
#     error = None
#     request.session.flush()
#     if request.method == 'POST':
#         username = request.POST.get('username', '').strip()
#         password = request.POST.get('password')
#         try:
#             print(f"Trying to log in with username: '{username}'")
#             # admin = Admin.objects.get(username=username)
#             admin = Admin.objects.get(name=username)
#             # Plain text password check (not secure)
#             if password == admin.password:
#                 request.session['admin_logged_in'] = True
#                 request.session['admin_id'] = admin.admin_id
#                 return redirect(reverse('admin_dashboard'))
#             else:
#                 error = 'Invalid username or password.'
#         except Admin.DoesNotExist:
#             error = 'Invalid username or password.'
#     return render(request, 'dashboard/admin_login.html', {'error': error})


# def admin_login(request):
#     error = None
#     if request.method == 'POST':
#         username = request.POST.get('username')  # or 'name' if your form uses 'name'
#         password = request.POST.get('password')
#         try:
#             admin = Admin.objects.get(name=username)  # changed from username=username
#             # ...password check logic...
#             if password == admin.password:
#                     request.session['admin_logged_in'] = True
#                     request.session['admin_id'] = admin.admin_id
#                     return redirect(reverse('admin_dashboard'))
#             else:
#                     error = 'Invalid username or password.'
#         except Admin.DoesNotExist:
#             # ...handle error...
#             error = 'Invalid username or password.'
#     return render(request, 'dashboard/admin_login.html', {'error': error})
# def admin_login(request):
#     error = None
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             admin = Admin.objects.get(name=username)
#             # admin = Admin.objects.get(name=username)
#             if password == admin.password:
#                 request.session['admin_logged_in'] = True
#                 request.session['admin_id'] = admin.admin_id  # <-- use admin_id, not id
#                 return redirect(reverse('admin_dashboard'))  # Redirect to dashboard
#             else:
#                 error = 'Invalid username or password.'
#         except Admin.DoesNotExist:
#             error = 'Invalid username or password.'
#     return render(request, 'dashboard/admin_login.html', {'error': error})
def admin_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            admin = Admin.objects.get(name=username)
            if password == admin.password:
                request.session['admin_logged_in'] = True
                request.session['admin_id'] = admin.admin_id
                return redirect(reverse('admin_dashboard'))  # This will navigate!
            else:
                error = 'Invalid username or password.'
        except Admin.DoesNotExist:
            error = 'Invalid username or password.'
    return render(request, 'dashboard/admin_login.html', {'error': error})


# def user_login(request):
#     error = None
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             error = 'Invalid username or password.'
#     return render(request, 'dashboard/user.html', {'error': error, 'user_login': True})


def get_all_coupons():
    coupons = Coupon.objects.all()
    return [
        {
            'id': c.coupon_id,
            'code': c.coupon_code,
            'expiry': c.expiry_date,
            'discount': c.discount_percentage,
            'max_usage': c.max_usage,
        }
        for c in coupons
    ]

def get_next_coupon_id():
    last_coupon = Coupon.objects.order_by('-coupon_id').first()
    if not last_coupon:
        return 'C001'
    last_id = int(last_coupon.coupon_id[1:])
    return f'C{last_id+1:03d}'

def insert_coupon(discount_percentage):
    coupon_id = get_next_coupon_id()
    coupon_code = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
    expiry_date = timezone.now().date() + timezone.timedelta(days=7)
    max_usage = 2
    Coupon.objects.create(
        coupon_id=coupon_id,
        coupon_code=coupon_code,
        expiry_date=expiry_date,
        discount_percentage=discount_percentage,
        max_usage=max_usage
    )
    return coupon_id

@csrf_exempt
def add_coupon(request):
    if request.method == 'POST':
        discount = request.POST.get('discount_percentage')
        try:
            coupon_id = insert_coupon(float(discount))
            return JsonResponse({'success': True, 'coupon_id': coupon_id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def coupons(request):
    coupons_list = get_all_coupons()
    return render(request, 'dashboard/coupons.html', {"coupons": coupons_list})


# def admin_dashboard(request):
#     if not request.session.get('admin_logged_in'):
#         return redirect(reverse('admin_login'))
#     products_list = [
#         {"number": i+1, "name": f"Product {i+1}", "image": f"https://picsum.photos/seed/prod{i+1}/80/80"}
#         for i in range(10)
#     ]
#     coupons_list = get_all_coupons()
#     return render(request, 'dashboard/admin.html', {"products_count": len(products_list), "coupons_count": len(coupons_list)})

# def admin_dashboard(request):
#     # ...
#     # Example where it might be used (e.g., for redirection if not logged in)
#     if not request.user.is_authenticated or not request.user.is_staff: # Assuming admin_login is for staff
#         return redirect(reverse('admin_login')) # <--- This is where the error occurs
#     # ...
#     return render(request, 'core/admin_dashboard.html')

# def admin_dashboard(request):
#     if not request.session.get('admin_logged_in'):
#         return redirect(reverse('admin_login'))
#     # ... your dashboard logic ...
#     return render(request, 'dashboard/admin.html')
def admin_dashboard(request):
    if not request.session.get('admin_logged_in'):
        return redirect(reverse('admin_login'))
    return render(request, 'dashboard/admin.html')

def franchise_dashboard(request):
    return render(request, 'dashboard/franchise.html')


def lead_dashboard(request):
    return render(request, 'dashboard/lead.html')


def marketing_dashboard(request):
    return render(request, 'dashboard/marketing.html')


def user_dashboard(request):
    return render(request, 'dashboard/user.html')


def admin_logout(request):
    request.session.flush()
    return redirect(reverse('admin_login'))


def products(request):
    products_list = [
        {"number": i+1, "name": f"Product {i+1}", "image": f"https://picsum.photos/seed/prod{i+1}/80/80"}
        for i in range(10)
    ]
    return render(request, 'dashboard/products.html', {"products": products_list})



def add_franchise(request):
    if request.method == 'POST':
        form = FranchiseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # or wherever you want to go after adding
    else:
        form = FranchiseForm()
    return render(request, 'dashboard/add_franchise.html', {'form': form})

@csrf_exempt
def add_franchise(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact_email = request.POST.get('contact_email')
        if name and address and contact_email:
            Franchise.objects.create(name=name, address=address, contact_email=contact_email)
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Missing fields'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

@csrf_exempt
def add_marketing_member(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        if name and email:
            MarketingTeamMember.objects.create(name=name, email=email, phone=phone)
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Missing fields'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

@csrf_exempt
def add_review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '')
        if name and rating:
            Review.objects.create(name=name, rating=rating, comment=comment)
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'error': 'Missing fields'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def get_reviews(request):
    reviews = Review.objects.order_by('-created_at')[:10]
    count = Review.objects.count()
    avg_rating = Review.objects.all().aggregate(Avg('rating'))['rating__avg'] or 0
    data = {
        'success': True,
        'count': count,
        'avg_rating': avg_rating,
        'reviews': [
            {'name': r.name, 'rating': r.rating, 'comment': r.comment, 'created_at': r.created_at.strftime('%Y-%m-%d')} for r in reviews
        ]
    }
    return JsonResponse(data)


def user_signup(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        otp = request.POST.get('otp')
        session_otp = request.session.get('signup_otp')
        if password1 != password2:
            error = 'Passwords do not match.'
        elif otp != session_otp:
            error = 'Invalid OTP.'
        elif AppUser.objects.filter(username=username).exists():
            error = 'Username already exists.'
        elif AppUser.objects.filter(email=email).exists():
            error = 'Email already exists.'
        else:
            AppUser.objects.create(username=username, email=email, password=password1)
            del request.session['signup_otp']
            return redirect('user_login')
    return render(request, 'dashboard/user_signup.html', {'error': error})

# def send_signup_otp(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         otp = str(random.randint(100000, 999999))
#         request.session['signup_otp'] = otp
#         # Send OTP to email (simulate for now)
#         # send_mail('Your OTP', f'Your OTP is {otp}', settings.DEFAULT_FROM_EMAIL, [email])
#         return JsonResponse({'success': True, 'otp': otp})
#     return JsonResponse({'success': False})

def user_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = AppUser.objects.get(username=username)
            if password == user.password:
                request.session['user_logged_in'] = True
                request.session['user_id'] = user.id
                return redirect(reverse('home'))  # Redirect to homepage after login
            else:
                error = 'Invalid username or password.'
        except AppUser.DoesNotExist:
            error = 'Invalid username or password.'
    return render(request, 'dashboard/user.html', {'error': error})
@csrf_exempt
def send_signup_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if not email:
            return JsonResponse({'success': False, 'error': 'No email provided'})
        otp = str(random.randint(100000, 999999))
        # Save OTP to session or DB as needed
        try:
            send_mail(
                'Your Signup OTP',
                f'Your OTP is: {otp}',
                'your_email@gmail.com',
                [email],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'})