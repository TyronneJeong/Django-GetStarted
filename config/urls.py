from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from users import views as user_views

urlpatterns = [
    path('', include('blog.urls')), # include urls.py file in blog
    path('register/', user_views.register, name="register"), # include urls.py file in apps
    path('profile/', user_views.profile, name="profile"), # profile
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"), # login
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"), # logout
    path('polls/', include('polls.urls')), # include urls.py file in apps
    path('admin/', admin.site.urls),
]
