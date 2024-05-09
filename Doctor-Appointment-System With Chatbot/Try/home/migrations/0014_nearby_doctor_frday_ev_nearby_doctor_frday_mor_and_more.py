# Generated by Django 4.1 on 2022-11-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_nearby_doctor_lag_spoken_nearby_doctor_repo_fee'),
    ]

    operations = [
        migrations.AddField(
            model_name='nearby_doctor',
            name='frday_ev',
            field=models.CharField(default='10', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nearby_doctor',
            name='frday_mor',
            field=models.CharField(default='11', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nearby_doctor',
            name='monday_ev',
            field=models.CharField(default='1', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nearby_doctor',
            name='monday_mor',
            field=models.CharField(default='13', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nearby_doctor',
            name='satday_ev',
            field=models.CharField(default='23', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nearby_doctor',
            name='satday_mor',
            field=models.CharField(default='1', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nearby_doctor',
            name='sunday_ev',
            field=models.CharField(default='2', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nearby_doctor',
            name='sunday_mor',
            field=models.CharField(default='21', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nearby_doctor',
            name='thursday_ev',
            field=models.CharField(default='3', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nearby_doctor',
            name='thursday_mor',
            field=models.CharField(default='4', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nearby_doctor',
            name='tuesday_ev',
            field=models.CharField(default='5', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nearby_doctor',
            name='tuesday_mor',
            field=models.CharField(default='14', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nearby_doctor',
            name='wedday_ev',
            field=models.CharField(default='15', max_length=122),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nearby_doctor',
            name='wedday_mor',
            field=models.CharField(default='10', max_length=122),
            preserve_default=False,
        ),
    ]
