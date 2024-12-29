# filepath: /Users/sergiusnyah/AfroVerb/backend/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import CustomRegisterView, upload_profile_picture, update_profile, protected_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', CustomRegisterView.as_view(), name='custom_registration'),
    path('auth/social/', include('allauth.socialaccount.urls')),
    path('upload/profile-picture/', upload_profile_picture, name='upload_profile_picture'),
    path('profile/', update_profile, name='profile'),
    path('protected/', protected_view, name='protected_view'),  # Add this line
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)