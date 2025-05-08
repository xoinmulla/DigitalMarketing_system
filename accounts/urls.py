from django.urls import path
from .views import home, campaign_list, create_campaign
from .views import ad_list, create_ad,track_click
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views 
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # This line is attempting to use a 'home' view
    path('campaigns/', campaign_list, name='campaign_list'),
    path('create/', create_campaign, name='create_campaign'),
    path('ads/', ad_list, name='ad_list'),
    path('ads/create/', create_ad, name='create_ad'),
    path('ads/click/<int:ad_id>/', track_click, name='track_click'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', accounts_views.register, name='accounts/register'),

    # Forgot password
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('home/',accounts_views.home, name='home'),  # This will define the profile page



]
