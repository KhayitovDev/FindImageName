from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import images_detail_view, LanguagesAPIView, get_next_image


urlpatterns = [
    path('languages/', LanguagesAPIView.as_view(), name='languages'),
    path('images/<int:pk>/', images_detail_view, name='images'),
    path('images/<int:pk>/', get_next_image, name='next_image')
    
]
