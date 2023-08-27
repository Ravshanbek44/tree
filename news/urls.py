from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.NewsListAPIView.as_view()),
    path('news/<int:pk>/', views.NewsDetailAPIView.as_view()),
    path('for-users/', views.ForUsersListAPIView.as_view())
]
