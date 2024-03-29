# Generated by Django 4.1.7 on 2024-02-01 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0003_post_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='user',
        ),
        migrations.AddField(
            model_name='reply',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор отклика'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply_post', to='board.post'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='text',
            field=models.TextField(verbose_name='Текст отклика'),
        ),
    ]
