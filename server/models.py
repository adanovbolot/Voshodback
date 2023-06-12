from django.db import models


class EvotorUsers(models.Model):
    class Meta:
        verbose_name = 'Пользователи Эвотор'
        verbose_name_plural = 'Пользователи Эвотор'

    userId = models.CharField(
        verbose_name='UserID',
        max_length=100,
    )
    token = models.CharField(
        verbose_name='Токен',
        max_length=250,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.userId}"


class EvotorToken(models.Model):
    class Meta:
        verbose_name = 'Эвотор токен'
        verbose_name_plural = 'Эвотор токены'

    userId = models.CharField(
        verbose_name='UserID',
        max_length=100,
        # unique=True
    )
    token = models.CharField(
        verbose_name='Токен',
        max_length=250,
        blank=True,
        null=True,
        # unique=True
    )

    def __str__(self):
        return f"{self.userId}, {self.token}"


class Shops(models.Model):
    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    uuid = models.CharField(
        verbose_name='uuid',
        max_length=200,
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=200,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    code = models.CharField(
        verbose_name='Код',
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.name} {self.address}"


class EvotorOperator(models.Model):
    class Meta:
        verbose_name = 'Эвотор Оператор'
        verbose_name_plural = 'Эвотор Операторы'

    uuid = models.CharField(
        verbose_name='uuid',
        max_length=200,
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    code = models.CharField(
        verbose_name='Код',
        max_length=100,
        blank=True,
        null=True
    )
    stores = models.CharField(
        verbose_name='Магазин',
        max_length=200,
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=100
    )

    def __str__(self):
        return f"{self.name} {self.stores}"


class Terminal(models.Model):
    class Meta:
        verbose_name = 'Терминал'
        verbose_name_plural = 'Терминалы'

    uuid = models.CharField(
        verbose_name='UUID',
        max_length=200,
        null=True,
        blank=True
    )
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        null=True,
        blank=True
    )
    store_uuid = models.CharField(
        verbose_name='UUID магазина',
        max_length=200,
        null=True,
        blank=True
    )
    timezone_offset = models.IntegerField(
        verbose_name='Смещение часового пояса',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    uuid = models.CharField(
        max_length=100,
        verbose_name="Уникальный идентификатор"
    )
    code = models.CharField(
        max_length=100,
        verbose_name="Код"
    )
    bar_codes = models.JSONField(
        default=list,
        verbose_name="Штрих-коды"
    )
    alco_codes = models.JSONField(
        default=list,
        verbose_name="Алкокоды"
    )
    name = models.CharField(
        max_length=200,
        verbose_name="Наименование"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )
    quantity = models.IntegerField(
        verbose_name="Количество"
    )
    cost_price = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        verbose_name="Себестоимость"
    )
    measure_name = models.CharField(
        max_length=50,
        verbose_name="Единица измерения"
    )
    tax = models.CharField(
        max_length=50,
        verbose_name="Налог"
    )
    allow_to_sell = models.BooleanField(
        verbose_name="Разрешено к продаже"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    article_number = models.CharField(
        max_length=50,
        verbose_name="Артикул"
    )
    parent_uuid = models.CharField(
        max_length=100,
        verbose_name="Идентификатор родителя"
    )
    group = models.BooleanField(
        verbose_name="Группа"
    )
    type = models.CharField(
        max_length=50,
        verbose_name="Тип"
    )
    alcohol_by_volume = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Крепость алкоголя"
    )
    alcohol_product_kind_code = models.IntegerField(
        verbose_name="Код вида алкогольной продукции"
    )
    tare_volume = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Объем тары"
    )

    def __str__(self):
        return f"{self.name}"
