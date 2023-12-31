# Generated by Django 4.2.3 on 2023-07-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_remove_settings_contacts_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_image')),
                ('description', models.TextField()),
                ('created', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
