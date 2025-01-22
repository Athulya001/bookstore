from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookonapp/', include('bookonapp.urls')),  # Link to the store app URLs
]

