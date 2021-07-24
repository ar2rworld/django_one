# Generated by Django 3.2 on 2021-07-24 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_statistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('account_created_date', models.DateField()),
                ('last_loged_date', models.DateTimeField()),
            ],
        ),
    ]