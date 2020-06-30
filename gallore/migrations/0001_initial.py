# Generated by Django 3.0.7 on 2020-06-29 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=30)),
                ('description', models.TextField()),
                ('image_url', models.ImageField(blank=True, default='image_url', upload_to='images/')),
                ('categories', models.ManyToManyField(to='gallore.categories')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallore.Location')),
            ],
        ),
    ]
