# views.py
from .models import UserDetails, MedicineReminder
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


def base(request):
    return render(request, 'base.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)  # Use 'email' as the username field
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Incorrect login credentials. Please try again.')
            return render(request, 'login.html')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user, created = User.objects.get_or_create(username=email)
        if not created:
            messages.error(request, 'This user already exists. Please choose a different email.')
            return render(request, 'signup.html')
        user.set_password(password)
        user.save()
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def home(request):
    return render(request, 'home.html')

def upload_details(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        hospital_name = request.POST.get('hospital_name', 'No Name')
        hospital_address = request.POST.get('hospital_address', 'No Address')
        doctor_name = request.POST.get('doctor_name', 'No Name')
        disease = request.POST.get('disease', 'No Disease')
        fees = request.POST.get('fees', 0)
        image_type = request.POST.get('image_type', 'Other')
        date = request.POST.get('date', timezone.now())
        image = request.FILES.get('image')

        if name and email and image:
            UserDetails.objects.create(
                name=name,
                email=email,
                hospital_name=hospital_name,
                hospital_address=hospital_address,
                doctor_name=doctor_name,
                disease=disease,
                fees=fees,
                image_type=image_type,
                date=date,
                image=image
            )
            return redirect('history')
        else:
            # Handle invalid form data, e.g., show an error message
            pass

    return render(request, 'upload_details.html')

def history(request):
    details = UserDetails.objects.all()
    return render(request, 'history.html', {'details': details})

from django.shortcuts import render, redirect
from .models import MedicineReminder  # Import your MedicineReminder model
from django.contrib.auth.decorators import login_required  # Add this import

@login_required  # This decorator ensures the user is logged in to access the view
def medicine_reminders(request):
    if request.method == 'POST':
        # Handle the form submission
        medicine_name = request.POST.get('medicine_name')
        quantity = request.POST.get('quantity')
        reminder_datetime = request.POST.get('reminder_datetime')

        # Create a new MedicineReminder object and save it to the database
        MedicineReminder.objects.create(
            user=request.user,
            medicine_name=medicine_name,
            quantity=quantity,
            reminder_datetime=reminder_datetime
        )
        return redirect('medicine_reminders')

    reminders = MedicineReminder.objects.filter(user=request.user)
    return render(request, 'medicine_reminders.html', {'reminders': reminders})
