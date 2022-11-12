from django.db import models


class Human(models.Model):
    name = models.CharField("Имя", max_length=20)
    age = models.PositiveIntegerField()
    gender = models.CharField("Пол", max_length=20)
    hobby = models.CharField("Хобби", max_length=35)
    profession = models.CharField("Профессия", max_length=35)

    def __str__(self):
        return self.name, self.gender, self.hobby, self.profession

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"


class Kid(models.Model):
    name = models.CharField("Имя", max_length=20)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    gender = models.CharField("", max_length=20)

    def __str__(self):
        return self.name, self.gender

    class Meta:
        verbose_name = "Ребенок"
        verbose_name_plural = "Дети"


class Icecream(models.Model):
    taste = models.CharField("Вкус", max_length=20)
    topping = models.CharField("Посыпка", max_length=30)
    foundation = models.CharField("Основа(рожок или посуда)",max_length=35)

    def __str__(self):
        return self.taste, self.topping, self.foundation

    class Meta:
        verbose_name = "Мороженое"
        verbose_name_plural = "Мороженые"


class Icecreamkiosk(models.Model):
    place = models.CharField("Место нахождения", max_length=30)
    years = models.PositiveSmallIntegerField("Сколько лет киоску", default=7)
    name = models.CharField("Название киоска", max_length=35)

    def __str__(self):
        return self.place, self.name

    class Meta:
        verbose_name = "Киоск"
        verbose_name_plural = "Киоски"