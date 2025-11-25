from django.db import models

class Student(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    middle_name = models.CharField(max_length=100, blank=True, verbose_name="Отчество")
    birth_year = models.IntegerField(verbose_name="Год рождения")
    group_number = models.CharField(max_length=10, verbose_name="Номер группы")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"