from django.db import models


# Create your models here.
# Создаем таблицу категорий
class Category(models.Model):
    category_name = models.CharField(max_length=64)  # то что главнее пишем раньше, потому что продукт

    # привязывается к категориям

    def __str__(self):
        return str(self.category_name)  # прописывается чтобы название категорий и продуктов прописывалось
        # нормально без объекта


# Создаем таблицу продукта
class Product(models.Model):
    product_name = models.CharField(max_length=256)
    product_des = models.TextField()
    product_price = models.FloatField()
    product_count = models.IntegerField()  # сколько у нас на складе есть товара
    product_photo = models.ImageField()
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)  # потому что это подкатегория нами
    # созданного класса Category, дается ключ ForeignKey, и нужно указать on_delete = models.CASCADE,
    # чтобы мы могли отвязать от главной таблицы
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product_name)


# Создаем таблицу корзины
class Cart(models.Model):
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)  # опять идет связка с классом Product,
    # который юзер будет добавлять в корзину из продуктов
    user_pr_count = models.IntegerField()  # что выбрал юзер в корзине
