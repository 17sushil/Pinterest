from django.urls import path
from . import views

app_name = 'boards'

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('create/', views.board_create, name='board_create'),
    path('<int:board_id>/', views.board_detail, name='board_detail'),
]
