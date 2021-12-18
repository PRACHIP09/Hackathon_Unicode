# Generated by Django 3.2.9 on 2021-12-18 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0014_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Role',
            field=models.CharField(choices=[('SELLER', 'SELLER'), ('BUYER', 'BUYER')], default='BUYER', max_length=255),
        ),
    ]
