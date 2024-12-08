from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('product/<int:pk>', views.product_page),  # Int - преобразователь пути, указывает что значение которое будет
    # передано через url целочисленное. pk - имя переменной, может называться как угодно, оно будет передано обработчик
    # view.В данном случае там будет айди товара
    path('category/<int:pk>', views.category_page)
]
