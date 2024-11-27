from django.contrib import admin
from django.urls import path, include
from accounts import views  
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('index/', views.index_view, name='index'),
    path('base/', views.base_view, name='base'),
    path('jobs/templetes/', include('jobs.urls')),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('', LogoutView.as_view(template_name='login.html'), name='index'),
    
      
]
