# Generated by Django 4.1 on 2022-12-11 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_regusers_doc_pat'),
    ]

    operations = [
        migrations.CreateModel(
            name='health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood', models.IntegerField()),
                ('suger_lvl', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]