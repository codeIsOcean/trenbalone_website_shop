from django.shortcuts import render
from .models import Category, Product, Cart


# Create your views here.
# Главная страница
def home_page(request):
    # Достаем данные из БД
    products = Product.objects.all()  # products мы сами создали переменную, objects зарезервированный уже метод
    categories = Category.objects.all()
    # Передаем данные на FrontEnd
    context = {     # context это означает что мы передаем из бэк энд во фронт
        'products': products,  # значение словаря берется из бд, ключ сами прописываем,
        # так как все данные во фронт по запросу гет передаются в виде словарей
        'categories': categories
    }

    return render(request, 'home.html', context)


