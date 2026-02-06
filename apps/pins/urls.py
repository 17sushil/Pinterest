from django.urls import path
from . import views

app_name = 'pins'

urlpatterns = [
    path('create/', views.pin_create, name='pin_create'),
    path('<int:pin_id>/', views.pin_detail, name='pin_detail'),
]
