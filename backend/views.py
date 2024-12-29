from rest_framework import generics
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, PasswordResetView
from rest_framework.response import Response
from rest_framework import status
import logging
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods, csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .forms import UserProfileForm

# Set up logging
logger = logging.getLogger(__name__)

ALLOWED_FILE_TYPES = ['image/jpeg', 'image/png']

class CustomRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = response.data.get('user')
        if user:
            # Custom logic: Log registration and send a welcome email
            logger.info(f"New user registered: {user['username']}")
            # send_welcome_email(user['email'])  # Uncomment and implement this function
        return response

class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = response.data.get('user')
        if user:
            # Custom logic: Log login activity
            logger.info(f"User logged in: {user['username']}")
        return response

class CustomPasswordResetView(PasswordResetView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        email = request.data.get('email')
        if email:
            # Custom logic: Log password reset request
            logger.info(f"Password reset requested for email: {email}")
        return response

@require_http_methods(["POST"])
def registration_view(request):
    # Handle the POST request here
    return HttpResponse("Registration successful!")

@csrf_exempt
@require_http_methods(["POST"])
def upload_profile_picture(request):
    file = request.FILES.get('file')
    if file and file.content_type in ALLOWED_FILE_TYPES:
        file_name = default_storage.save(f'profile_pictures/{file.name}', ContentFile(file.read()))
        file_url = default_storage.url(file_name)
        return JsonResponse({'file_url': file_url}, status=201)
    else:
        return JsonResponse({'error': 'Invalid file type'}, status=400)

def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            logger.info(f"User profile updated: {request.user.username}")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

def protected_view(request):
    return JsonResponse({'message': 'This is a protected view'})