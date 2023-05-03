# Generated by Django 4.1.2 on 2023-03-01 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='sayt')),
                ('content', models.CharField(max_length=256)),
                ('slug', models.SlugField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.IntegerField()),
                ('price_type', models.CharField(choices=[('USD', 'USD'), ('RUB', 'RUB'), ('EUR', 'EUR'), ('UZS', 'UZS')], max_length=16)),
                ('len', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('is_bed', models.BooleanField(default=False)),
                ('bed_len', models.IntegerField(blank=True, null=True)),
                ('bed_width', models.IntegerField(blank=True, null=True)),
                ('bed_height', models.IntegerField(blank=True, null=True)),
                ('update_dt', models.DateTimeField(auto_now=True)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('ctg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagesapp.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('update_dt', models.DateTimeField(auto_now=True)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagesapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dona', models.IntegerField(default=1)),
                ('umumiy', models.IntegerField(default=0)),
                ('update_dt', models.DateTimeField(auto_now=True)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pagesapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
