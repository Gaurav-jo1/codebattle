# Generated by Django 4.1.3 on 2022-11-05 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0004_remove_advocates_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advocates',
            name='username',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
