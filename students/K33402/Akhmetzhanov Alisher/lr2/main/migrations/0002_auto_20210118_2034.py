# Generated by Django 3.1.2 on 2021-01-18 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelroom',
            name='free',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userroom',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_history', to=settings.AUTH_USER_MODEL),
        ),
    ]
