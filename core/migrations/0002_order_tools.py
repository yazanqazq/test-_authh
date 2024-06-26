# Generated by Django 5.0.3 on 2024-04-02 12:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('status_field', models.CharField(choices=[('Shipped', 'Shipped'), ('Not Shipped', 'Not Shipped')], max_length=30)),
                ('shipping_type', models.CharField(choices=[('Express Shipping', 'Express Shipping'), ('Standard shipping', 'Standard shipping')], max_length=30)),
                ('total', models.FloatField(default=0)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.CharField(blank=True, max_length=500, null=True)),
                ('quantity', models.IntegerField()),
                ('item_price', models.FloatField()),
                ('shipping_cost', models.FloatField()),
                ('image_tools', models.ImageField(upload_to='')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tools', to='core.address')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tools', to=settings.AUTH_USER_MODEL)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Tools', to='core.order')),
            ],
        ),
    ]
