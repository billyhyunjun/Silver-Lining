from django.db import models


# Create your models here.
class Order(models.Model):
    STATUS_CHOICES = (
        ("A", "주문접수"),
        ("R", "준비중"),
        ("C", "준비완료"),
    )

    order_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    order_menu = models.JSONField(default=list)
    total_price = models.PositiveIntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
