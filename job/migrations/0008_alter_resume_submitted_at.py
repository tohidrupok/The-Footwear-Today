# Generated by Django 5.0.3 on 2024-05-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_resume_contact_resume_email_resume_expected_salary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='submitted_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
