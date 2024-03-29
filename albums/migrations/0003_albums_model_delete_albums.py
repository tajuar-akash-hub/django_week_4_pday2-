# Generated by Django 5.0 on 2024-01-19 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_alter_albums_album_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='albums_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50)),
                ('album_release_date', models.DateField()),
                ('album_rating', models.CharField(choices=[('three', '3'), ('five', '5'), ('two', '2'), ('one', '1'), ('four', '4')], max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='albums',
        ),
    ]
