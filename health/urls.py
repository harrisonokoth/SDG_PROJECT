# health/urls.py
from django.urls import path
from .views import login_view, logout_view,signup_view ,dashboard, register_mother, register_child, update_health, health_reports, signup_view  # Import the signup_view
from django.contrib.auth.views import LoginView
from .views import dashboard
from . import views
from .views import registered_children
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register_mother, name='register_mother'),
    path('register/child/', register_child, name='register_child'),
    path('register-child/<int:mother_id>/', views.register_child, name='register_child'),
    path('update-health/<int:mother_id>/', views.update_health, name='update_health'),
     path('dashboard/', dashboard, name='dashboard'),
    path('reports/', views.health_reports, name='health_reports'),
    path('mothers/', views.registered_mothers, name='registered_mothers'),  # New URL for registered mothers
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('children/', registered_children, name='registered_children'),
]

