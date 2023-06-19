# Generated by Django 4.1.7 on 2023-05-21 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_productorder_amount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='order',
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductOrder',
        ),
        migrations.DeleteModel(
            name='Stuff',
        ),
    ]