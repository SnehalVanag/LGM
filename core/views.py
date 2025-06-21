from django.shortcuts import render, redirect
from django.urls import reverse
from datetime import datetime, timedelta
import random, string
from .forms import FranchiseForm, ProductForm
from .models import Franchise, Coupon, Product
from django.utils import timezone
from .models import Admin
from django.contrib.auth.hashers import check_password, make_password
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
from django.shortcuts import get_object_or_404
from .forms import ProductForm
from .models import Franchise
from .models import Staff
from .forms import StaffForm
from django.contrib.auth import get_user_model
# from django.contrib.auth.decorators import login_required
from .models import Franchise
from .forms import FranchiseForm  # You need to create this form
from django.shortcuts import render, redirect
from .models import Staff
from .forms import StaffForm

def edit_franchise(request, pk):
    franchise = get_object_or_404(Franchise, pk=pk)
    if request.method == 'POST':
        form = FranchiseForm(request.POST, instance=franchise)
        if form.is_valid():
            form.save()
            messages.success(request, 'Franchise updated successfully.')
            return redirect('marketing_dashboard')  # Change to your dashboard url name
    else:
        form = FranchiseForm(instance=franchise)
    return render(request, 'dashboard/edit_franchise.html', {'form': form, 'franchise': franchise})

def delete_franchise(request, pk):
    franchise = get_object_or_404(Franchise, pk=pk)
    if request.method == 'POST':
        franchise.delete()
        messages.success(request, 'Franchise deleted successfully.')
        return redirect('marketing_dashboard')  # Change to your dashboard url name
    return render(request, 'dashboard/confirm_delete_franchise.html', {'franchise': franchise})

def franchise_products(request):
    products = Product.objects.all()  # or filter as needed
    return render(request, 'dashboard/products.html', {
        'products': products,
        'disable_actions': True,
    })
@csrf_exempt
def add_staff(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            address = data.get('address') # Assuming this is office_address from your models
            contact_email = data.get('contact_email')
            phone_number = data.get('phone_number')
            # You'll likely need to link to existing User and Franchise
            # For example, if franchise_id is part of your data, or derived from authenticated user
            # franchise_id = data.get('franchise_id')
            # franchise = Franchise.objects.get(id=franchise_id)
            # user_for_staff = User.objects.create_user(username=contact_email, password='some_default_password') # Or link to existing user

            # Example: Assuming you get franchise_id and a user for this staff from the request or session
            franchise_id = data.get('franchise_id') # Example: You might send this from frontend
            user_id = data.get('user_id') # Example: You might send this from frontend (e.g., if staff logs in)

            # --- IMPORTANT: Replace with actual logic to get franchise and user ---
            # This part depends heavily on how you link staff to users and franchises
            # If a new user is created for staff:
            # new_staff_user = User.objects.create_user(username=contact_email, email=contact_email, password='some_temp_password')
            # franchise = Franchise.objects.get(pk=franchise_id) # Replace with actual way to get franchise

            # For now, let's assume some dummy linkage if you're just testing the view:
            # (REMOVE OR REPLACE IN PRODUCTION)
            # Find the franchise (e.g., from authenticated admin's franchise or from request data)
            # You mentioned franchise admin: request.user.franchise if you have OneToOneField
            # For demo:
            try:
                franchise_instance = Franchise.objects.first() # DANGEROUS: Get first franchise (for testing only)
                # Or get it from the requesting user if the admin is linked to a franchise
                # franchise_instance = request.user.franchise # If your User model has a OneToOne relationship to Franchise
            except Franchise.DoesNotExist:
                return JsonResponse({'error': 'No franchise found to associate staff with'}, status=500)

            # Find or create a User for this Staff entry (important for login later)
            # A staff member typically has a user account linked
            # You might create a default password or require one from the frontend
            try:
                # Attempt to find by email, otherwise create
                staff_user, created = User.objects.get_or_create(username=contact_email, defaults={'email': contact_email, 'password': 'default_password'})
                # For created user, set password appropriately or hash it
                if created:
                    staff_user.set_password('default_password') # Hash and save password
                    staff_user.save()
            except Exception as e:
                return JsonResponse({'error': f'Could not manage user for staff: {str(e)}'}, status=500)


            staff = Staff.objects.create(
                user=staff_user, # Link to the User instance
                franchise=franchise_instance, # Link to the Franchise instance
                full_name=name, # Use name from frontend
                email=contact_email,
                phone_number=phone_number,
                role=data.get('role', 'Staff') # Assuming 'role' is also passed or defaulted
            )
            return JsonResponse({'message': 'Staff added successfully', 'staff_id': staff.staff_id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON in request body'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': f'Missing data field: {e}'}, status=400)
        except Exception as e:
            # This catches any other unexpected errors in your view logic
            print(f"An unexpected error occurred: {e}") # This will print to your terminal
            return JsonResponse({'error': 'An internal server error occurred'}, status=500)
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('role')
        if name and email and role:
            Staff.objects.create(name=name, email=email, role=role)
            staff_count = Staff.objects.count()
            return JsonResponse({'success': True, 'staff_count': staff_count})
    return JsonResponse({'success': False})
def edit_staff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('marketing_dashboard')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'dashboard/edit_staff.html', {'form': form, 'staff': staff})

def delete_staff(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('marketing_dashboard')
    return render(request, 'dashboard/delete_staff.html', {'staff': staff})

def delete_branch(request, branch_id):
    branch = get_object_or_404(Franchise, id=branch_id)
    if request.method == 'POST':
        branch.delete()
        return redirect('franchise_dashboard')
    return redirect('franchise_dashboard')


def add_branch(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        area = request.POST.get('area')
        contact_email = request.POST.get('contact_email')
        # Save new branch
        Franchise.objects.create(
            name=name,
            address=address,
            area=area,
            contact_email=contact_email
        )
        return redirect('franchise_dashboard')  # or your dashboard view name
    return redirect('franchise_dashboard')

def marketing_dashboard(request):
    products_count = Product.objects.count()
    franchises_count = Franchise.objects.count()
    staff_count = Staff.objects.count()
    user_count = AppUser.objects.count()
    franchises = Franchise.objects.all()
    # franchises_count = franchises.count()

    context = {
        'products_count': products_count,
        'franchises_count': franchises_count,
        'staff_count': staff_count,
        'user_count': user_count,
        'franchises': franchises,
        # Add other context variables as needed
    }
    return render(request, 'dashboard/marketing.html', context)

# def marketing_dashboard(request):
#     staff_list = Staff.objects.all()
#     staff_count = staff_list.count()
#     user_count = AppUser.objects.count()
#     franchises = Franchise.objects.all()

#     # User = get_user_model()
#     # user_count = User.objects.filter(is_active=True).count()
#     return render(request, 'dashboard/marketing.html', {
#         'staff_list': staff_list,
#         'staff_count': staff_count,
#         'user_count': user_count,
#         'franchises': franchises,
#     # return render(request, 'dashboard/marketing.html')
#   })

def coupon_list(request):
    coupons = Coupon.objects.all()
    return render(request, 'dashboard/coupon_list.html', {'coupons': coupons})
def home(request):
    return render(request, 'dashboard/home.html')


def manager_dashboard(request):
    return render(request, 'dashboard/home.html')


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')  # or wherever you want to go after saving
    else:
        form = ProductForm()
    return render(request, 'dashboard/add_product.html', {'form': form})


# def admin_login(request):
#     error = None
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         try:
#             admin = Admin.objects.get(name=username)
#             if password == admin.password:
#                 request.session['admin_logged_in'] = True
#                 request.session['admin_id'] = admin.admin_id
#                 return redirect(reverse('admin_dashboard'))  # This will navigate!
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
                request.session['is_core_admin'] = True  # <-- Add this line
                request.session['admin_name'] = admin.name  # <-- And this line
                return redirect(reverse('admin_dashboard'))
            else:
                error = 'Invalid username or password.'
        except Admin.DoesNotExist:
            error = 'Invalid username or password.'
    return render(request, 'dashboard/admin_login.html', {'error': error})


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


def admin_dashboard(request):
    franchises = Franchise.objects.all()
    if not request.session.get('admin_logged_in'):
        return redirect(reverse('admin_login'))
    products_count = Product.objects.count()
    coupons_count = Coupon.objects.count()
    franchises_count = Franchise.objects.count()
    marketing_members = MarketingTeamMember.objects.all()
    marketing_members_count = marketing_members.count()
    user_count = AppUser.objects.count()
    return render(request, 'dashboard/admin.html', {
        'products_count': products_count,
        'coupons_count': coupons_count,
        'franchises_count': franchises_count,
        'franchises': franchises,
        'marketing_members': marketing_members,
        'marketing_members_count': marketing_members_count,
        'user_count': user_count,
    })

def products_view(request):
    products = Product.objects.all()
    return render(request, 'dashboard/products.html', {'products': products})
# @login_required

def lead_dashboard(request):
    return render(request, 'dashboard/lead.html')

def user_dashboard(request):
    return render(request, 'dashboard/user.html')

def admin_logout(request):
    request.session.flush()
    return redirect(reverse('admin_login'))

def products(request):
    products_list = Product.objects.all()
    return render(request, 'dashboard/products.html', {"products": products_list})

def add_franchise(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact_email = request.POST.get('contact_email')
        phone_number = request.POST.get('phone_number')
        print('Phone:', phone_number)  # Debug: See if value is received

        Franchise.objects.create(
            name=name,
            address=address,
            contact_email=contact_email,
            phone_number=phone_number
        )
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

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

@csrf_exempt
def delete_franchise(request, id):
    if request.method == 'POST':
        Franchise.objects.filter(id=id).delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

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
        username = request.POST['username']
        email = request.POST.get('email')
        password = request.POST['password']
        is_active = request.POST.get('is_active', 'True') == 'True'
        if AppUser.objects.filter(username=username).exists():
            error = 'Username already exists.'
        elif AppUser.objects.filter(email=email).exists():
            error = 'Email already exists.'
        else:
            AppUser.objects.create(
                username=username,
                email=email,
                password=make_password(password),
                is_active=is_active,
            )
            return redirect('user_login')  # Fixed: use correct login url name
    return render(request, 'dashboard/user_signup.html', {'error': error})

def user_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = AppUser.objects.get(username=username)
            if check_password(password, user.password):
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

def marketing_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # You can implement your own authentication logic here
        # For now, just allow any username/password for demo
        if username and password:
            # In a real app, check against MarketingTeamMember or similar
            return redirect('marketing_dashboard')
        else:
            error = 'Invalid username or password.'
    return render(request, 'dashboard/admin_login.html', {'error': error, 'marketing_login': True})

def franchise_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Implement your franchise authentication logic here
        # For now, just allow any username/password for demo
        if username and password:
            # In a real app, check against Franchise or similar
            return redirect('franchise_dashboard')
        else:
            error = 'Invalid username or password.'
    return render(request, 'dashboard/admin_login.html', {'error': error, 'franchise_login': True})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')  # This will go to /products/
    else:
        form = ProductForm()
    return render(request, 'dashboard/add_product.html', {'form': form})

def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'dashboard/add_product.html', {'form': form, 'update': True})

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render(request, 'dashboard/delete_product.html', {'product': product})

def user_signup(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST.get('email')
        password = request.POST['password']
        is_active = request.POST.get('is_active', 'True') == 'True'
        if AppUser.objects.filter(username=username).exists():
            error = 'Username already exists.'
        elif AppUser.objects.filter(email=email).exists():
            error = 'Email already exists.'
        else:
            AppUser.objects.create(
                username=username,
                email=email,
                password=make_password(password),
                is_active=is_active,
            )
            return redirect('user_login')  # Fixed: use correct login url name
    return render(request, 'dashboard/user_signup.html', {'error': error})

def franchise_dashboard(request):
    franchises = Franchise.objects.all()
    return render(request, 'dashboard/franchise.html', {
        'franchises': franchises,
        'admin_user': request.user,
    })




def franchise_dashboard(request):
    staff_list = Staff.objects.all()
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('franchise_dashboard')  # Replace with your dashboard URL name
    else:
        form = StaffForm()
    return render(request, 'dashboard/franchise.html', {
        'staff_list': staff_list,
        'form': form,
        # ...other context variables...
    })
