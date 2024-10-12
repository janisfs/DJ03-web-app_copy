from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),  # Укажи функцию для отображения страницы новостей
]
