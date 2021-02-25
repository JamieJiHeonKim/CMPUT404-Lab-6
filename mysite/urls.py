from django.contrib import admin
from django.urls import include, path

urlspatterns = [
        path('admin/', admin.site.urls),
        path('polls/', include('polls.urls')),
        ]

