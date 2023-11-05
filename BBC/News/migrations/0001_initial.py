# Generated by Django 4.2.7 on 2023-11-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=6000)),
                ('reporter', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='News_images')),
                ('date_reported', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
    ]
