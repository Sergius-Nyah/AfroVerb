# filepath: /Users/sergiusnyah/AfroVerb/backend/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import CustomRegisterView, upload_profile_picture
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', CustomRegisterView.as_view(), name='custom_registration'),
    path('auth/social/', include('allauth.socialaccount.urls')),
    path('upload/profile-picture/', upload_profile_picture, name='upload_profile_picture'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)