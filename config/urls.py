from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', views.health_check, name='health-check'),
    path('api/', include('core.urls')),
]
