from django.shortcuts import render
from .models import Category, Product, Cart


# Create your views here.
# Главная страница
def home_page(request):
    # Достаем данные из БД
    products = Product.objects.all()  # products мы сами создали переменную, objects зарезервированный уже метод
    categories = Category.objects.all()
    # Передаем данные на FrontEnd
    context = {  # context это означает что мы передаем из бэк энд во фронт
        'products': products,  # значение словаря берется из бд, ключ сами прописываем,
        # так как все данные во фронт по запросу гет передаются в виде словарей
        'categories': categories
    }

    return render(request, 'home.html', context)


# Вывод товаров по выбранной категорий
def category_page(request, pk):
    # достаем выбранную категорию
    category = Category.objects.get(id=pk)
    # фильтруем товары по категорий
    products = Product.objects.filter(product_category=category)
    print(products)
    # Передаем данные на Frontend
    context = {'category': category, 'products': products}

    return render(request, 'category.html', context)


# Вывод определенного товара
def product_page(request, pk):
    # Вывод выбранного товара
    product = Product.objects.get(id=pk)
    # передаем данные во Frontend
    context = {'product': product}

    return render(request, 'product.html', context)
