from django.db import models


class Genre(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        """Строковое представление модели
        """
        return self.name
    
    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"