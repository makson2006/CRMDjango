from django.db import models

class SalesForecast(models.Model):
    product = models.ForeignKey('crm_core.Product', on_delete=models.CASCADE)  # Продукт
    forecast_date = models.DateField()  # Дата прогнозу
    forecast_quantity = models.PositiveIntegerField()  # Прогнозована кількість продажів
    created_at = models.DateTimeField(auto_now_add=True)  # Дата створення запису

    def __str__(self):
        return f"Forecast for {self.product.name} on {self.forecast_date}"
