# Generated by Django 4.1.7 on 2023-06-14 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0012_delete_productcategory_alter_product_alco_codes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='alco_codes',
            field=models.JSONField(default=list, null=True, verbose_name='Алкокоды'),
        ),
        migrations.AlterField(
            model_name='product',
            name='alcohol_by_volume',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Крепость алкоголя'),
        ),
        migrations.AlterField(
            model_name='product',
            name='alcohol_product_kind_code',
            field=models.IntegerField(null=True, verbose_name='Код вида алкогольной продукции'),
        ),
        migrations.AlterField(
            model_name='product',
            name='allow_to_sell',
            field=models.BooleanField(null=True, verbose_name='Разрешено к продаже'),
        ),
        migrations.AlterField(
            model_name='product',
            name='article_number',
            field=models.CharField(max_length=50, null=True, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='product',
            name='bar_codes',
            field=models.JSONField(default=list, null=True, verbose_name='Штрих-коды'),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(default=1, max_length=100, verbose_name='Код'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='cost_price',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True, verbose_name='Себестоимость'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.BooleanField(default=False, null=True, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='product',
            name='measure_name',
            field=models.CharField(max_length=50, null=True, verbose_name='Единица измерения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='parent_uuid',
            field=models.CharField(max_length=100, null=True, verbose_name='Идентификатор родителя'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(null=True, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tare_volume',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Объем тары'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax',
            field=models.CharField(max_length=50, null=True, verbose_name='Налог'),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(max_length=50, null=True, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='product',
            name='uuid',
            field=models.CharField(default=1, max_length=100, verbose_name='Уникальный идентификатор'),
            preserve_default=False,
        ),
    ]