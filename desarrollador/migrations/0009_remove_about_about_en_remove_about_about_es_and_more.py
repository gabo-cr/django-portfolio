# Generated by Django 4.1.5 on 2023-01-20 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desarrollador', '0008_about_about_en_about_about_es_contact_name_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='about_en',
        ),
        migrations.RemoveField(
            model_name='about',
            name='about_es',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name_es',
        ),
        migrations.RemoveField(
            model_name='project',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='project',
            name='name_es',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='name_es',
        ),
    ]
