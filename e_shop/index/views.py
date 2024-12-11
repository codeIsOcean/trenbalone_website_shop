from django.shortcuts import render, redirect
from .models import Category, Product, Cart
from .forms import RegForm
from django.views import View
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


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


class Register(View):
    template_name = 'registration/register.html'

    # Выдача формы
    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_name, context)

    # Получение инфы с формы
    def post(self, request):
        form = RegForm(request.POST)

        # Если данные корректны
        if form.is_valid():
            username = form.clean_username()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            # создаем объект класса User
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()

            # Авторизуем пользователя
            login(request, user)
            return redirect('/')

        # если данные некорректны
        context = {'form': RegForm, 'message': 'Пароль или почта неверны'}
        return render(request, self.template_name, context)


# поиск
def search(request):
    if request.method == 'POST':
        get_product = request.POST.get('search')

        if Product.objects.get(product_name__iregex=get_product):  # iregex - ищем все в lower case
            searched_product = Product.objects.get(product_name__iregex=get_product)
            return redirect(f'/product/{searched_product.id}')
        else:
            return redirect('/')

