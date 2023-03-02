# Generated by Django 2.2.22 on 2023-03-02 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=70)),
                ('Email', models.EmailField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
            ],
        ),
    ]