# Generated by Django 4.1.6 on 2023-03-15 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operand1', models.FloatField()),
                ('operand2', models.FloatField()),
                ('defined', models.BooleanField()),
                ('result', models.FloatField()),
                ('agree', models.BooleanField()),
                ('PYAnswer', models.FloatField()),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.operator')),
            ],
        ),
    ]