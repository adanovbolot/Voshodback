# Generated by Django 4.1.7 on 2023-06-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_alter_receipt_id_receipt'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(unique=True, verbose_name='UUID')),
                ('group', models.BooleanField(verbose_name='Группа')),
                ('hasVariants', models.BooleanField(verbose_name='Имеет варианты')),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='Тип')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код')),
                ('barCodes', models.JSONField(blank=True, null=True, verbose_name='Штрихкоды')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('costPrice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Себестоимость')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Количество')),
                ('measureName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Единица измерения')),
                ('tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Налог')),
                ('allowToSell', models.BooleanField(blank=True, null=True, verbose_name='Разрешена продажа')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('articleNumber', models.CharField(blank=True, max_length=255, null=True, verbose_name='Артикул')),
                ('parentUuid', models.UUIDField(blank=True, null=True, verbose_name='UUID родителя')),
                ('alcoCodes', models.JSONField(blank=True, null=True, verbose_name='Коды алкогольной продукции')),
                ('alcoholByVolume', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Крепость алкоголя')),
                ('alcoholProductKindCode', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код вида алкогольной продукции')),
                ('tareVolume', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Объем тары')),
                ('classificationCode', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код классификации')),
                ('allowPartialSell', models.BooleanField(blank=True, null=True, verbose_name='Разрешена частичная продажа')),
                ('quantityInPackage', models.IntegerField(blank=True, null=True, verbose_name='Количество в упаковке')),
            ],
            options={
                'verbose_name': 'Категория товара',
                'verbose_name_plural': 'Категории товаров',
            },
        ),
        migrations.CreateModel(
            name='TerminalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(verbose_name='UUID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('lastName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('patronymicName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон')),
                ('code', models.CharField(blank=True, max_length=255, null=True, verbose_name='Код')),
                ('stores', models.JSONField(blank=True, null=True, verbose_name='Магазины')),
                ('role', models.CharField(blank=True, max_length=255, null=True, verbose_name='Роль')),
            ],
            options={
                'verbose_name': 'Пользователь терминала',
                'verbose_name_plural': 'Пользователи терминалов',
            },
        ),
    ]
