# Generated by Django 3.2.9 on 2022-12-01 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_userinfo_user_createtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_createtime', models.DateField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=64, unique=True)),
                ('customer_address', models.CharField(max_length=64, unique=True)),
                ('customer_mobile', models.CharField(max_length=64, unique=True)),
                ('business_name', models.CharField(max_length=64, unique=True)),
                ('business_address', models.CharField(max_length=64, unique=True)),
                ('business_mobile', models.CharField(max_length=64, unique=True)),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business', to='myApp.userinfo')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='myApp.userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('order_product_cost', models.DecimalField(decimal_places=2, max_digits=9)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.orderinfo')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.product')),
            ],
        ),
    ]