from django.urls import path
from . import views

urlpatterns = [
    path('', views.work_list, name='work_list'),
    path('<int:pk>/', views.work_detail, name='work_detail'),

]
