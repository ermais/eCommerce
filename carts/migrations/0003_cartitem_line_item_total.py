# Generated by Django 2.1.5 on 2019-06-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20190609_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='line_item_total',
            field=models.DecimalField(decimal_places=2, default=19.9, max_digits=12),
            preserve_default=False,
        ),
    ]