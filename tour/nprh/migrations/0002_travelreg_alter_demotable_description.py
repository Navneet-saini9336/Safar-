# Generated by Django 4.1.1 on 2022-11-13 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nprh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='travelreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('adharno', models.CharField(max_length=200)),
                ('phoneno', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('startingdate', models.CharField(max_length=200)),
                ('enddate', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='demotable',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]