# Generated by Django 5.2.4 on 2025-07-21 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_first_app', '0004_chaicertificate_chaireview_store'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaireview',
            name='rating',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5'),
        ),
    ]
