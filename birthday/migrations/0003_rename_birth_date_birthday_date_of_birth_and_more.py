# Generated by Django 5.1.6 on 2025-02-20 09:30

import django.core.validators
import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0002_alter_birthday_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='birthday',
            old_name='birth_date',
            new_name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AlterField(
            model_name='staff',
            name='phone_number',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator('^\\d{11}$', message='Phone number must be exactly 11 digits.')]),
        ),
        migrations.AlterField(
            model_name='staff',
            name='profile_image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddConstraint(
            model_name='staff',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('email'), name='unique_lower_email'),
        ),
    ]
