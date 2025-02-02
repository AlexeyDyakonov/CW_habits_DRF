from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    """Модель пользователя"""

    username = None
    email = models.EmailField(
        verbose_name="Почта", unique=True, help_text="Укажите почту"
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        **NULLABLE,
        help_text="Введите номер телефона",
    )
    city = models.CharField(
        max_length=50, verbose_name="Город", **NULLABLE, help_text="Введите город"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        **NULLABLE,
        help_text="Загрузите фото",
    )
    tg_chat_id = models.CharField(
        max_length=50,
        **NULLABLE,
        verbose_name="TG чат ID",
        help_text="Укажите чат ID в Telegram",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
