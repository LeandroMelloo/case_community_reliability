from django.db import models

# Create your models here.


class CatBreeds(models.Model):
    """Cat object."""

    id_breeds = models.CharField(max_length=255, verbose_name="Id Breeds")
    name = models.CharField(max_length=255, verbose_name="Nome")
    origin = models.CharField(max_length=255, verbose_name="Origem")
    temperament = models.TextField(verbose_name="Temperamento")
    description = models.TextField(verbose_name="Descrição")
    date_joined = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Data Criação")
    date_modified = models.DateTimeField(
        auto_now_add=True, verbose_name="Data Modificação")

    class Meta:
        managed = True
        db_table = "cat_breeds"
        verbose_name = "Cat Breed"
        verbose_name_plural = "Cats Breeds"
        ordering = ["id"]

    def __str__(self):
        return self.name
