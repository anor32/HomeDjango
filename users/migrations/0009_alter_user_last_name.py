# Generated by Django 5.0.13 on 2025-04-01 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_avatar_alter_user_date_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Anonymous', max_length=150, verbose_name='фамилия'),
        ),
    ]
