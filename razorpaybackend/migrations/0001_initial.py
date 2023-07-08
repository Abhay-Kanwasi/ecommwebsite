# Generated by Django 4.2.2 on 2023-07-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=100, verbose_name='Payment ID')),
                ('order_id', models.CharField(max_length=100, verbose_name='Order ID')),
                ('signature_id', models.CharField(max_length=100, verbose_name='Signature ID')),
                ('amount', models.IntegerField(max_length=100, verbose_name='Amount')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
