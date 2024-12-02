from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    USER = "user", "Пользователь"
    MODERATOR = "moderator", "Модератор"
    ADMIN = "admin", "Админ"


class ReviewUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="email")
    role = models.CharField(
        max_length=100,
        default=UserRole.USER,
        choices=UserRole.choices,
        verbose_name="Роль",
    )
    bio = models.TextField(
        null=True,
        blank=True,
        verbose_name="Биография",
    )

    class Meta(AbstractUser.Meta):
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
