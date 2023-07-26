# Generated by Django 4.2.3 on 2023-07-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0011_albums'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('descriprion', models.TextField()),
            ],
            options={
                'verbose_name': 'ОБРАЩЕНИЕ',
                'verbose_name_plural': 'ОБРАЩЕНИЯ',
            },
        ),
    ]
