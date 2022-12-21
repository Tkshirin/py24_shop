from django.contrib.auth import get_user_model
from django.db import models
from applications.product.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.owner


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rating')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating')
    rating = models.SmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ],
        blank=True, null=True
    )

    def __str__(self):
        return self.owner


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner


class Favorite(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites')

    def __str__(self):
        return self.owner
