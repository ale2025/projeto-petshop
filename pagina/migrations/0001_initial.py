# Generated by Django 3.0.2 on 2020-01-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
