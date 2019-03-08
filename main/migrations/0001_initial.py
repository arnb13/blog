# Generated by Django 2.1.5 on 2019-03-02 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('published', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]