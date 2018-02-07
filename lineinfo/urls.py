from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^buslist/', views.BusLineList.as_view(),name='bus_line_list'),
    url(r'^bus/', views.BusList.as_view(),name='bus_model_list')
]