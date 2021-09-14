from django.db import models


# Create your models here.
class Category(models.Model):
    Naimenovanie = models.CharField("Категория", max_length=50)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Edizm(models.Model):
    Naimenovanie = models.CharField("ЕдИзм", max_length=50)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "ЕдИзм"
        verbose_name_plural = "ЕдИзм"


class NamKabinet(models.Model):
    Naimenovanie = models.CharField("Название кабинета", max_length=100)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "Название кабинета"
        verbose_name_plural = "Название кабинета"



class Kabinet(models.Model):
    Naimenovanie = models.CharField("Кабинет", max_length=50)
    NamKabinet = models.ForeignKey(NamKabinet, verbose_name="Название кабинета", on_delete=models.CASCADE)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинет"


SOSTOYANIE = (
    ('рабочий', 'рабочий'),
    ('не рабочий', 'не рабочий')
)



class Corps(models.Model):
    Naimenovanie = models.CharField("Учебный корпус", max_length=50)

    def __str__(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "Учебный корпус"
        verbose_name_plural = "Учебный корпус"



class NalichiTehniki(models.Model):
    Corps = models.ForeignKey(Corps, verbose_name="Учебный корпус", on_delete=models.CASCADE)
    Kabinet = models.ForeignKey(Kabinet, verbose_name="Кабинет", on_delete=models.CASCADE)
    NamKabinet = models.ForeignKey(NamKabinet, verbose_name="Тип Кабинета", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категории", on_delete=models.CASCADE)
    Edizm = models.ForeignKey(Edizm, verbose_name="Ед.изм.", on_delete=models.CASCADE, null=True)
    kodTMU = models.IntegerField(verbose_name="КодТМУ")
    Naimenovanie = models.CharField(max_length=255, verbose_name="Наименования", null=True)
    Kolich = models.IntegerField(verbose_name="Количество", default=1)
    sostoyanie = models.CharField(choices=SOSTOYANIE, verbose_name='Состояние', max_length=20, null=True)

    def _str_(self):
        return self.Naimenovanie

    class Meta:
        verbose_name = "Наличие техники"
        verbose_name_plural = "Наличие техники"


