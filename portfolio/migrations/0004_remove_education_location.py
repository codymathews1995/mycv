# Generated by Django 5.1.2 on 2024-10-31 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_rename_skills_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='location',
        ),
    ]