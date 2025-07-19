from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('create/', views.create, name='create-page'),
    # path('users-create/', views.UsersCreateView.as_view(), name='users-list-create'),
    # path('user/<int:pk>/', views.UserUpdateDelete.as_view(), name='user-update-delete'),
]

router = DefaultRouter()
router.register(r'users', views.UsersViewSet, basename='users')
urlpatterns += router.urls

