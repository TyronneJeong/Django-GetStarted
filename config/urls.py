from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')), # urls 파일을 include 시킨다.
    path('admin/', admin.site.urls),
]
