# Generated by Django 4.1.3 on 2022-11-05 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advocates',
            name='id',
        ),
        migrations.AlterField(
            model_name='advocates',
            name='username',
            field=models.CharField(default=1, max_length=200, primary_key=True, serialize=False),
        ),
    ]
