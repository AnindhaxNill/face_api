from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
     path('upload/', views.ImageUploadView.as_view(), name='image-upload'),
]