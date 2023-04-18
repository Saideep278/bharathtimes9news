# Generated by Django 4.1.7 on 2023-04-05 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_dnews_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('tagline', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('desc', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('time', models.TimeField()),
                ('media', models.FileField(upload_to='media')),
            ],
        ),
        migrations.DeleteModel(
            name='DNews',
        ),
    ]
