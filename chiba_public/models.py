from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Facility(models.Model):
    name = models.CharField(max_length=60, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_kana = models.CharField(max_length=128)
    address = models.CharField(max_length=60)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Facility'
        verbose_name_plural = 'Facilities'
