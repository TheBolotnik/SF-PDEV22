# Generated by Django 4.1.7 on 2023-06-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_remove_category_uniq_category_name_news_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]