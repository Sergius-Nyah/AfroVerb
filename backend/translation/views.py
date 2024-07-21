from django.shortcuts import render
import requests
import pyrebase
from .forms import UserForm
from django.shortcuts import render
import requests
import pyrebase

config = {
    "apiKey": "your-api-key",
    "authDomain": "your-auth-domain",
    "databaseURL": "your-database-url",
    "projectId": "your-project-id",
    "storageBucket": "your-storage-bucket",
    "messagingSenderId": "your-messaging-sender-id",
    "appId": "your-app-id"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def sign_up(request):
    form = UserForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = auth.create_user_with_email_and_password(email, password)
        return render(request, 'sign_up.html')
    else:
        return render(request, 'error.html', {'form': form})

def sign_in(request):
    form = UserForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = auth.sign_in_with_email_and_password(email, password)
        return render(request, 'sign_in.html')
    else:
        return render(request, 'error.html', {'form': form})

def reset_password(request):
    email = request.POST.get('email')
    auth.send_password_reset_email(email)
    return render(request, 'reset_password.html')

# Add this link to Frontend template: <a href="{% url 'social:begin' 'google-oauth2' %}">Sign in with Google</a>