# Generated by Django 4.0.2 on 2022-02-06 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('milage', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]