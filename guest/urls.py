from django.contrib import admin
from django.urls import path
from . import views as guest_view
from django.urls import include, re_path, path

app_name = 'guest'
urlpatterns = [
    re_path('', guest_view.start, name='start'),
    path('register/', guest_view.register, name='register'),
    path('login/', guest_view.user_login, name='login'),
    re_path(r'login/home/', guest_view.home, name='home'),
    re_path(r'login/select/<int:res_id>/', guest_view.select, name='select'),
    # url(r'profile/^$', guest_view.profile, name='profile'),
    re_path(r'login/edit/<int:res_id>/', guest_view.edit, name='edit'),
    re_path(r'login/confirm/<int:res_id>/', guest_view.confirm, name='confirm'),
    re_path(r'login/cancel/<int:res_id>/', guest_view.cancel, name='cancel'),
    re_path(r'login/pdf/<int:res_id>/', guest_view.generate_pdf, name='pdf'),
    re_path(r'login/bookings/', guest_view.bookings, name='bookings'),
    path('logout/', guest_view.logout_view, name='logout'),
]