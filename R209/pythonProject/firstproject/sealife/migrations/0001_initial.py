# Generated by Django 4.0.4 on 2022-04-29 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specie', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('date_discovered', models.DateField()),
                ('size', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('lifespan', models.IntegerField()),
                ('depth', models.IntegerField()),
                ('locations', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(blank='false', on_delete=django.db.models.deletion.CASCADE, to='sealife.categories')),
            ],
        ),
    ]
