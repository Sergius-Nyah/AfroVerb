from rest_framework import generics
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, PasswordResetView
from rest_framework.response import Response
from rest_framework import status
import logging
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

# Set up logging
logger = logging.getLogger(__name__)

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