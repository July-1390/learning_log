from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    # Страница со списком всех тем.
    path('topics/', views.topics, name='topics'),
    # Страница отдельных тем
    path('topics/<int:topic_id>/', views.topic, name='topic'),
 ]