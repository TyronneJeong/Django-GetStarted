from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')), # include urls.py file in apps
    path('admin/', admin.site.urls),
]
