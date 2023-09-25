# Generated by Django 4.1.6 on 2023-03-15 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_populate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expression',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='calculator.operator'),
        ),
    ]