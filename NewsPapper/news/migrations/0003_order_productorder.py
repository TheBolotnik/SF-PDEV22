# Generated by Django 4.1.7 on 2023-04-05 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_stuff_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('time_out', models.DateTimeField(null=True)),
                ('cost', models.FloatField(default=0.0)),
                ('pickup', models.BooleanField(default=False)),
                ('complete', models.BooleanField(default=False)),
                ('stuff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.stuff')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.product')),
            ],
        ),
    ]