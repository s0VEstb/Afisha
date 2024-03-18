from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='category'
    )

    def __str__(self):
        return self.title


STARS = ((i, str(i)) for i in range(1, 6))

class Review(models.Model):
    text = models.CharField(max_length=50)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    stars = models.IntegerField(choices=STARS,null=True, blank=True)

    def __str__(self):
        return self.text
