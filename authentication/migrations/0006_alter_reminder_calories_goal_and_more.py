# Generated by Django 4.2.10 on 2024-02-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_caloriesburned_delete_dailyset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='calories_goal',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='step_goal',
            field=models.PositiveIntegerField(),
        ),
    ]
