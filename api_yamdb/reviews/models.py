from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models

from review_user.models import ReviewUser


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название категории')
    slug = models.SlugField(
        unique=True, db_index=True, verbose_name='slug категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название жанра')
    slug = models.SlugField(
        unique=True, db_index=True, verbose_name='slug жанра')
    description = models.TextField(verbose_name='описание жанра')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title


class Title(models.Model):
    title = models.TextField(
        max_length=200, verbose_name='Название произведения', db_index=True)
    year = models.IntegerField(verbose_name='Год публикации', null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория',
        null=True,

    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр',
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return f'{self.title}, {self.category}, {self.genre}, {self.year}'


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    author = models.ForeignKey(
        ReviewUser, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(10)])

    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)
        unique_together = ('author', 'title')

    def __str__(self):
        return self.text


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(
        ReviewUser, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.text
