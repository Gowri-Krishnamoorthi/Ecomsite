from django.db import models

# Create your models here.
class Products(models.Model):
      
      def __str__(self):
            return self.title

      title = models.CharField(max_length=200)
      price = models.FloatField()
      discount_price = models.FloatField()
      category = models.CharField(max_length=200)
      description = models.TextField()
      image = models.CharField(max_length=300)


class Order(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    zipcode = models.CharField(max_length=10)
    items = models.JSONField()  # Storing cart data as JSON

    def __str__(self):
        return f"Order by {self.name}"
