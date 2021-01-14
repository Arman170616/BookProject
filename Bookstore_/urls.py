
from django.contrib import admin
from django.urls import path, include #new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Pages.urls')),
    # User management
    path('accounts/', include('django.contrib.auth.urls')), # new

    path('accounts/', include('users.urls')), # new
]
