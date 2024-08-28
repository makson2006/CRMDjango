from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)  # Ім'я клієнта
    last_name = models.CharField(max_length=50)   # Прізвище клієнта
    email = models.EmailField(unique=True)        # Email
    phone_number = models.CharField(max_length=20, blank=True, null=True)  # Номер телефону
    address = models.TextField(blank=True, null=True)  # Адреса клієнта
    date_created = models.DateTimeField(auto_now_add=True)  # Дата створення запису

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=100)  # Назва продукту
    category = models.CharField(max_length=50)  # Категорія продукту
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Ціна продукту
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Собівартість продукту
    stock = models.PositiveIntegerField()  # Кількість товару на складі
    date_added = models.DateTimeField(auto_now_add=True)  # Дата додавання продукту

    def __str__(self):
        return self.name

    @property
    def margin(self):
        return self.price - self.cost  # Маржа продукту

class Sale(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)  # Клієнт
    product = models.ForeignKey('Product', on_delete=models.CASCADE)  # Продукт
    quantity = models.PositiveIntegerField()  # Кількість проданого продукту
    sale_date = models.DateTimeField(auto_now_add=True)  # Дата продажу
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Загальна сума продажу

    def __str__(self):
        return f"Sale of {self.product.name} to {self.customer.first_name} {self.customer.last_name}"

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.product.price  # Обчислення загальної суми продажу
        super().save(*args, **kwargs)
