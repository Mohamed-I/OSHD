# Generated by Django 3.2 on 2021-04-15 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('mid_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_recorded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
