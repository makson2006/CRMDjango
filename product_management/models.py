from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=50)  # Назва категорії
    description = models.TextField(blank=True, null=True)  # Опис категорії

    def __str__(self):
        return self.name

class ProductReview(models.Model):
    product = models.ForeignKey('crm_core.Product', on_delete=models.CASCADE)  # Продукт
    rating = models.PositiveIntegerField()  # Оцінка продукту (1-5)
    review_text = models.TextField()  # Текст відгуку
    review_date = models.DateTimeField(auto_now_add=True)  # Дата відгуку

    def __str__(self):
        return f"Review for {self.product.name} - Rating: {self.rating}"
