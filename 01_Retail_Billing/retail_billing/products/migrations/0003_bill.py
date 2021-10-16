# Generated by Django 3.1.4 on 2020-12-15 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_list', models.CharField(max_length=150)),
                ('qty_list', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=21)),
                ('bill_value', models.IntegerField(default=0)),
            ],
        ),
    ]