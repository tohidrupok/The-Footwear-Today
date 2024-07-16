# Generated by Django 5.0.3 on 2024-04-27 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_date', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('pdf_file', models.FileField(upload_to='publications/')),
            ],
        ),
    ]
