from django.urls import path
from . import views

urlpatterns = [
    path('browse/', views.browse_jobs, name='browse_jobs'),
    path('about/', views.about_us, name='about'),
]
