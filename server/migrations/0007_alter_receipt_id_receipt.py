# Generated by Django 4.1.7 on 2023-06-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_receipt_id_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='id_receipt',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='ID'),
        ),
    ]