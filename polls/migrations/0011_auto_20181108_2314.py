# Generated by Django 2.0.7 on 2018-11-08 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0010_auto_20180724_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='liked_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='faculty',
            name='dept',
            field=models.CharField(choices=[('sas', 'School of Advanced Sciences'), ('scse', 'School of Computing Science and Engineering')], default='', max_length=7),
        ),
    ]