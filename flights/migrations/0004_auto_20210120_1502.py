# Generated by Django 3.1.5 on 2021-01-20 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passenger'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('gender', models.CharField(max_length=64)),
                ('origin', models.CharField(max_length=64)),
                ('destination', models.CharField(max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='flight',
            name='duration',
        ),
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='Airport',
        ),
    ]
