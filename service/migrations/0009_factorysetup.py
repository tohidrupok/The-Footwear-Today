# Generated by Django 5.0.6 on 2024-07-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_alter_category_icon_alter_requirement_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactorySetup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='FactorySetup/')),
                ('contant', models.CharField(max_length=3000)),
                ('contant1', models.CharField(blank=True, max_length=3000, null=True)),
                ('contant2', models.CharField(blank=True, max_length=3000, null=True)),
                ('contant3', models.CharField(blank=True, max_length=3000, null=True)),
                ('pdf_file', models.FileField(blank=True, null=True, upload_to='FactorySetup/pdf')),
            ],
        ),
    ]
