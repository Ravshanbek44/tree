from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.TreeReportCreateAPIView.as_view()),
    path('docs/', views.DocsAPIView.as_view()),
    path('docs-status/', views.DocsUpdateAPIView.as_view())
]
