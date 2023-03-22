from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('add-photos/', views.add_photos, name='add-photos'),
    path('photos/<int:pk>', views.manage_photo, name='manage-photo'),
]
