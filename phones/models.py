from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exist = models.BooleanField()
    slug = models.SlugField(max_length=255)
    # TODO: Добавьте требуемые поля
    pass
