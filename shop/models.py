from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_total_products(self):
        return self.products.count()


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number_in_stock = models.IntegerField()
    date_published = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    is_book = models.BooleanField(default=False)
    is_magazine = models.BooleanField(default=False)
    is_record = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def remove_one_from_stock(self):
        self.number_in_stock -= 1
        self.save()

    def format_price(self):
        return '{:,.2f}'.format(self.price)


class Book(Product):
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Magazine(Product):
    publisher = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Record(Product):
    artist = models.CharField(max_length=150)

    def __str__(self):
        return self.name
