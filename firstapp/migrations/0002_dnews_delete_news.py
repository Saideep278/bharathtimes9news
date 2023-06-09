# Generated by Django 4.1.7 on 2023-04-05 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('time', models.TimeField()),
                ('media', models.FileField(upload_to='media')),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
