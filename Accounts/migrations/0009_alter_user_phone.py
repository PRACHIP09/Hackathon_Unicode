# Generated by Django 3.2.9 on 2021-12-17 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default=0, max_length=15, unique=True),
        ),
    ]
