from django.contrib import admin
from django.urls import path, include
from stations import views

urlpatterns = [
    path('', views.public_home),
    path('staff/', views.staff_dashboard),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]