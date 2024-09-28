from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import MotherRegistrationForm, ChildRegistrationForm, MotherForm, HealthRecordForm
from .models import Mother, Child
from django.contrib.auth.models import User
from django.contrib import messages



# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid credentials')
    return render(request, 'registration/login.html')


# Signup view
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
    return render(request, 'registration/signup.html')


# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')


# Register a new mother
def register_mother(request):
    if request.method == 'POST':
        form = MotherRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mother registered successfully.")
            return redirect('registered_mothers')
    else:
        form = MotherRegistrationForm()
    return render(request, 'health/register_mother.html', {'form': form})


# Register a new child and associate them with a mother
def register_child(request):
    if request.method == 'POST':
        form = ChildRegistrationForm(request.POST)
        if form.is_valid():
            child = form.save()
            messages.success(request, "Child registered successfully.")
            return redirect('registered_children')
    else:
        form = ChildRegistrationForm()

    mothers = Mother.objects.all()  # For the dropdown of mothers
    return render(request, 'health/register_child.html', {'form': form, 'mothers': mothers})


# Update health information for a mother
def update_health(request, mother_id):
    mother = get_object_or_404(Mother, pk=mother_id)
    if request.method == 'POST':
        form = MotherForm(request.POST, instance=mother)
        if form.is_valid():
            form.save()
            messages.success(request, "Health information updated successfully.")
            return redirect('dashboard')
    else:
        form = MotherForm(instance=mother)
    return render(request, 'health/update_health.html', {'form': form, 'mother': mother})


# View health reports, including overdue checkups
def health_reports(request):
    mothers = Mother.objects.all()
    overdue_checkups = mothers.filter(next_checkup_date__lt=timezone.now())
    return render(request, 'health/reports.html', {'overdue_checkups': overdue_checkups})


# Dashboard view for listing mothers and children
@login_required
def dashboard(request):
    mothers = Mother.objects.filter(next_checkup_date__lt=timezone.now())
    children = Child.objects.all()  # You can add filters based on vaccination status
    return render(request, 'health/dashboard.html', {
        'mothers': mothers,
        'children': children,
        'alerts': bool(mothers),  # Simplified alert check
    })


# View for registered mothers
def registered_mothers(request):
    mothers = Mother.objects.all()  # Fetch all registered mothers
    return render(request, 'health/registered_mothers.html', {'mothers': mothers})


# View for registered children
def registered_children(request):
    children = Child.objects.all()  # Fetch all registered children
    return render(request, 'health/registered_children.html', {'children': children})


# Record a new health record for a mother
def health_record(request):
    if request.method == 'POST':
        form = HealthRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Health record saved successfully.")
            return redirect('dashboard')
    else:
        form = HealthRecordForm()
    return render(request, 'health/register_health_record.html', {'form': form})
