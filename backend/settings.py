import os

from backend.afroverb.settings import BASE_DIR

# ...existing code...

MIDDLEWARE = [
    # ...existing middleware...
    'backend.middleware.ErrorHandlingMiddleware',
    'backend.middleware.LoggingMiddleware',
    'backend.middleware.AuthenticationMiddleware',
    # ...existing middleware...
]

INSTALLED_APPS = [
    # ...existing apps...
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'social_django',  # Add this line
    'yourapp',  # Add your app here
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'social_core.backends.google.GoogleOAuth2',  # Add this line
)

REST_USE_JWT = True

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True

# ...existing code...

# Email backend configuration for sending verification emails
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Google OAuth2 configuration
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    }
}

AUTH_USER_MODEL = 'yourapp.CustomUser'

MIDDLEWARE += [
    # ...existing code...
    'django_otp.middleware.OTPMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',  # Add this line
]

# Add social-auth-app-django settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<your-client-id>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<your-client-secret>'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ...existing code...
