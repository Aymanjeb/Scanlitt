from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from .views import add_user_profile


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/dashboard/', views.dashboard, name='dashboard'),

    path('add/', views.add_user_profile, name='add_user_profile'),
    path('edit_user_profile/<int:pk>/', views.edit_user_profile, name='edit_user_profile'),
    path('delete_user_profile/<int:pk>/', views.delete_user_profile, name='delete_user_profile'),
    path('edit_user_profile/<int:id>/edit_user_profile.html', views.dashboard, name='edit'),
]






