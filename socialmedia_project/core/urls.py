from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('feed/', views.feed_view, name='feed'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('admin/', admin.site.urls),  # <-- needs admin imported
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]
