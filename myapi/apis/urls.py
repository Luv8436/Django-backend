from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('devices/', views.get_devices , name="devices"),
    path('devices/<int:uid>', views.get_device_with_id),
    path('devices/<int:uid>/readings/<str:parameter>/', views.get_readings_time),
    path('devices-graph/', views.plot_graph),
]
