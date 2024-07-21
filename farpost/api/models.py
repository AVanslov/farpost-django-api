from django.db import models

MAX_LENGTH = 1000


class Author(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Add(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=MAX_LENGTH)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='adds'
    )
    views_count = models.IntegerField()
    position = models.IntegerField()

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ('title',)

    def __str__(self):
        return self.title
