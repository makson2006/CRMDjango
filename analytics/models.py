from django.db import models

class Dashboard(models.Model):
    name = models.CharField(max_length=100)  # Назва дашборду
    description = models.TextField(blank=True, null=True)  # Опис дашборду
    date_created = models.DateTimeField(auto_now_add=True)  # Дата створення

    def __str__(self):
        return self.name

class Report(models.Model):
    dashboard = models.ForeignKey('Dashboard', on_delete=models.CASCADE)  # Дашборд, до якого відноситься звіт
    report_date = models.DateField()  # Дата звіту
    data = models.JSONField()  # Дані звіту у форматі JSON

    def __str__(self):
        return f"Report for {self.dashboard.name} on {self.report_date}"
