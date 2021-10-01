from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('items/', views.getItems),
    path('items/create/', views.createItem),
    path('items/<int:pk>/update/', views.updateItem),
    path('items/<int:pk>/delete/', views.deleteItem),
    path('items/<int:pk>/', views.getItem),

    path('users/', views.getUsers),
    path('users/create/', views.createUser),
    path('users/<int:pk>/update/', views.updateUser),
    path('users/<int:pk>/delete/', views.deleteUser),
    path('users/<int:pk>/', views.getUser),

    path('auth/login', views.authLogin),
    path('auth/<int:pk>/logout', views.authLogout),
    path('auth/register', views.authReg),
]
