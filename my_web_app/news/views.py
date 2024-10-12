from django.shortcuts import render
from .models import News_post

def news_home(request):
    news = News_post.objects.all()  # Получаем все новости из базы данных
    return render(request, 'news/news_home.html', {'news': news})  # Укажи путь к шаблону
