# Generated by Django 3.1.2 on 2021-01-22 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210122_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='copies',
        ),
        migrations.RemoveField(
            model_name='bookreplica',
            name='replica',
        ),
        migrations.AddField(
            model_name='bookreplica',
            name='cipher',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='bookreplica',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bookreplica',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_copies', to='main.book'),
        ),
        migrations.DeleteModel(
            name='Replica',
        ),
    ]
