from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('kino_location.urls')),
    path('api/v1/auth', obtain_auth_token),
]
