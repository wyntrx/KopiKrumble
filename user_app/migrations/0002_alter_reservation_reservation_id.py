# Generated by Django 4.0.3 on 2022-04-01 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
