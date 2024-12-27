import random
import requests
import threading
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.hashers import make_password
from .forms import LoginForm, SignupForm
from .models import User, MembershipRequest, UserProfile, UserSubscription, CancellationRequest
from .fitness.models import FitnessBlogPost, WorkoutCategories, FitnessExercise, FitnessEquipment
from .nutrition.models import Recipe,Guide,Article,Essentials
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError

otp_storage = {}

def generate_otp():
    return str(random.randint(100000, 999999))

def landing(request):
    return render(request, 'main/landing.html')

def hit_chatbot_in_background():
    try:
        requests.get('http://127.0.0.1:8000/chatbot')  # Adjust the URL as needed
    except requests.RequestException as e:
        print(f'Error hitting /chatbot: {e}')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    auth_login(request, user)
                    
                    # Start a new thread to hit /chatbot in the background
                    threading.Thread(target=hit_chatbot_in_background).start()

                    return redirect('home')
                else:
                    return render(request, 'main/login.html', {'form': form, 'error': 'Invalid credentials'})
            except User.DoesNotExist:
                return render(request, 'main/login.html', {'form': form, 'error': 'User does not exist'})
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('landing')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            otp = generate_otp()
            email = form.cleaned_data['email']
            otp_storage[email] = otp  # Store the OTP

            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp}',
                'nutri.fit.web.customer@gmail.com',
                [email],
                fail_silently=False,
            )

            # Store form data in the session without 'confirm_password'
            signup_data = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'sex': form.cleaned_data['sex'],
                'age': form.cleaned_data['age'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password']  # Handle password securely
            }
            request.session['signup_data'] = signup_data

            return redirect('otp_verification')
        else:
            # Do not save form data in the session if form is not valid
            request.session.pop('signup_data', None)
    else:
        form = SignupForm()
    return render(request, 'main/signup.html', {'form': form})

def otp_verification(request):
    # Check if signup data exists in session
    if 'signup_data' not in request.session:
        return redirect('signup')  # Redirect to signup if no signup data is found

    if request.method == 'POST':
        email = request.session.get('signup_data', {}).get('email')
        otp = request.POST.get('otp')

        if email and otp == otp_storage.get(email):
            form_data = request.session.get('signup_data')
            if form_data:
                User.objects.create_user(
                    email=form_data['email'],
                    password=form_data['password'],  # Password is hashed by create_user
                    first_name=form_data['first_name'],
                    last_name=form_data['last_name'],
                    sex=form_data['sex'],
                    age=form_data['age']
                )
                del otp_storage[email]  # Remove the OTP after successful verification
                request.session.pop('signup_data', None)  # Clear the signup data
                return redirect('home')
        else:
            return render(request, 'main/otp_verification.html', {'error': 'Invalid OTP'})
    
    # Handle GET requests or if no POST data is submitted
    return render(request, 'main/otp_verification.html')


@login_required
def home(request):
    return render(request, 'main/home.html')

@login_required
def about_us(request):
    return render(request, 'main/about_us.html')

@login_required
def contact_us(request):
    return render(request, 'main/contact_us.html')

@login_required
def mental_fitness(request):
    blog_posts = FitnessBlogPost.objects.all().order_by('-date')  # Retrieves all posts, newest first
    return render(request, 'main/fitness/mental_fitness.html', {'blog_posts': blog_posts})

@login_required
def blog_detail(request, post_id):
    post = get_object_or_404(FitnessBlogPost, id=post_id)
    return render(request, 'main/fitness/blog_detail.html', {'post': post})

@login_required
def workouts(request, category_id=None):
    # Fetch all categories for breadcrumb navigation and to determine the first category
    categories = WorkoutCategories.objects.all()
    
    # Select the first category by default if no category_id is provided
    if category_id:
        selected_category = get_object_or_404(WorkoutCategories, id=category_id)
    else:
        selected_category = categories.first()  # Default to the first category if no category_id

    # Display only the selected category's workouts
    workout_categories = [selected_category] if selected_category else []

    return render(request, 'main/fitness/workouts.html', {
        'workout_categories': workout_categories,
        'categories': categories,
        'selected_category': selected_category,
    })

@login_required
def workout_detail(request, exercise_id):
    exercise = get_object_or_404(FitnessExercise, id=exercise_id)
    return render(request, 'main/fitness/workout_detail.html', {'exercise': exercise})

@login_required
def fitness_equipments(request):
    equipment_list = FitnessEquipment.objects.all()  # Fetch all equipment data
    return render(request, 'main/fitness/fitness_equipments.html', {'equipment_list': equipment_list})

@login_required
def recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'main/nutrition/recipes.html', {'content_list': recipes})

@login_required
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients_list = recipe.ingredients.split(', ')
    detailed_instructions_list = recipe.detailed_instructions.split('\n ')
    # print(ingredients_list)
    return render(request, 'main/nutrition/recipe_detail.html', {'recipe': recipe, 'ingredients_list': ingredients_list, 'detailed_instructions_list': detailed_instructions_list})

@login_required
def guides(request):
    guides = Guide.objects.all()
    return render(request, 'main/nutrition/guides.html', {'content_list': guides})

@login_required
def guide_detail(request, pk):
    guides = get_object_or_404(Guide, pk=pk)
    guide_list = guides.content.split('\n')
    # print(guide_list)
    return render(request, 'main/nutrition/guide_info.html', {'guides': guides, 'guide_list': guide_list})

@login_required
def expert_blogs_detail(request,pk):
    expert_blogs = get_object_or_404(Article, pk=pk)
    return render(request, 'main/expert_blog_info.html', {'expert_blogs': expert_blogs})


@login_required
def nutri_essentials(request):
    essentials = Essentials.objects.all()
    return render(request, 'main/nutrition/nutri_essentials.html', {'essentials': essentials})

@login_required
def expert_blogs(request):
    expert_blogs = Article.objects.all()
    return render(request, 'main/expert_blogs.html', {'content_list': expert_blogs})

@login_required
def membership(request):
    user_email = request.user.email
    user_id = request.user.id
    # print(user_id)
    return render(request, 'main/membership.html', {'user_email': user_email, 'user_id': user_id})


@login_required
def submit_membership_request(request):
    if request.method == "POST":
        email = request.POST.get("email")
        plan = request.POST.get("plan")
        subscription_type = request.POST.get("subscription_type")

        # Check if user already has a membership
        existing_membership = MembershipRequest.objects.filter(email=email, approved_status=True).exists()
        if existing_membership:
            return JsonResponse({
                "status": "error",
                "message": "You already have an active membership."
            })

        try:
            # Create a new membership request
            MembershipRequest.objects.create(email=email, plan=plan, subscription_type=subscription_type)

            # Send an email notification
            send_mail(
                subject=f"New Membership Request: {plan}",
                message=f"User with email {email} has requested to join the {plan} plan with a {subscription_type} subscription.",
                from_email='nutri.fit.web.customer@gmail.com',
                recipient_list=['nutri.fit.web.customer@gmail.com'],
                fail_silently=False,
            )

            # Return success response
            return JsonResponse({"status": "success", "message": "Membership request submitted successfully!"})
        except IntegrityError:
            return JsonResponse({
                "status": "error",
                "message": "An error occurred. It looks like you already have an active membership request."
            })

    return JsonResponse({"status": "error", "message": "Invalid request"})

@login_required
def my_account(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    user_subscription = UserSubscription.objects.filter(email=user.email).first()  # Adjusted to use email as a primary key

    return render(request, 'main/myaccount.html', {
        'user_profile': user_profile,
        'user_subscription': user_subscription,
    })

@login_required
def update_account(request):
    if request.method == 'POST':
        # Update or create user profile
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Update the profile fields
        user_profile.phone = phone
        user_profile.address = address
        user_profile.save()

        # Display a success message
        messages.success(request, 'Your profile has been updated successfully.', extra_tags='alert-success')
        return redirect('my_account')  # Redirect back to the account page
    
    return redirect('my_account')


@login_required
def cancel_subscription(request):
    if request.method == "POST":
        email = request.POST.get("email")
        reason = request.POST.get("reason")

        # Create a new CancellationRequest in the database
        CancellationRequest.objects.create(
            user=request.user,
            reason=reason,
            cancelled_status=False  # Initially set to False (Pending)
        )

        # Send cancellation email to admin
        send_mail(
            subject="Subscription Cancellation Request",
            message=f"User with email {email} wants to cancel their subscription.\nReason: {reason}",
            from_email=email,
            recipient_list=['nutri.fit.web.customer@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, "Your request to cancel the subscription has been sent successfully.")
        return redirect('my_account')

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)