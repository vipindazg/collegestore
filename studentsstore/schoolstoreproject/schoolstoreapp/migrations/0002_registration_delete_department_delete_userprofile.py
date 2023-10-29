# Generated by Django 4.2.6 on 2023-10-28 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolstoreapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
