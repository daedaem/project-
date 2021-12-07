# Generated by Django 3.2.9 on 2021-11-22 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0003_merge_0002_rate_0002_rating'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rate',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='rates',
        ),
        migrations.AddField(
            model_name='rating',
            name='rate',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_rates', to='movies.movie'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rates', to=settings.AUTH_USER_MODEL),
        ),
    ]
