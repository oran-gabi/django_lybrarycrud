# Generated by Django 5.0.7 on 2024-07-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
