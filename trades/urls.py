from django.urls import path
from . import views

urlpatterns = [
    path('region/', views.RegionListAPIView.as_view()),
    path('district/', views.DistrictListAPIView.as_view()),
    path('tree-classifier/', views.TreeClassifierListAPIView.as_view()),
    path('tree-type/', views.TypeTreeListAPIView.as_view()),
    path('delivery-company/', views.TreeDeliveryListAPIView.as_view()),
    path('trade/', views.TradeCreateAPIView.as_view()),
]
