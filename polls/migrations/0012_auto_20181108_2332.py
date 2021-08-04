# Generated by Django 2.0.7 on 2018-11-08 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0011_auto_20181108_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('direction', models.SmallIntegerField(choices=[(1, 'like'), (-1, 'dislike')], max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='liked_by',
        ),
        migrations.AddField(
            model_name='like',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='polls.Faculty'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]