from django.urls import path
from . import views

urlpatterns = [
    path('contract/', views.ContractCreateAPIView.as_view()),
    path('contract-with-partner/', views.ContractWithPartnerCreateAPIView.as_view())
]
