# Generated by Django 3.0 on 2020-04-17 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import farm.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crop', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.DecimalField(decimal_places=2, default=0.0, max_digits=300)),
                ('is_active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.Address')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ploting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crop.Crop')),
            ],
        ),
        migrations.CreateModel(
            name='Soil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='WaterResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField()),
                ('depth', models.IntegerField()),
                ('diameter', models.IntegerField()),
                ('income_rate', models.IntegerField()),
                ('available_water', models.IntegerField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Primary'), (2, 'Secondary')], default=1)),
                ('is_active', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to=farm.models.upload_file_path)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ploting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.Ploting')),
            ],
        ),
        migrations.CreateModel(
            name='Plots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.PositiveSmallIntegerField(choices=[(1, 'Full'), (2, 'Half')], default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.Farm')),
            ],
        ),
        migrations.AddField(
            model_name='ploting',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.Plots'),
        ),
        migrations.AddField(
            model_name='farm',
            name='soil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farm.Soil'),
        ),
        migrations.AddField(
            model_name='farm',
            name='water_resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='farm.WaterResource'),
        ),
    ]
