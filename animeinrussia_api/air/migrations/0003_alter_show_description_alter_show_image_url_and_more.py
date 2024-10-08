# Generated by Django 4.1.3 on 2022-11-23 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("air", "0002_show_sent_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="show",
            name="description",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="show",
            name="image_url",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="Image URL",
            ),
        ),
        migrations.AlterField(
            model_name="show",
            name="pub_date",
            field=models.DateTimeField(
                blank=True, default=None, null=True, verbose_name="Published date"
            ),
        ),
        migrations.AlterField(
            model_name="show",
            name="sent_at",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="show",
            name="title_orig",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="Original title",
            ),
        ),
        migrations.AlterField(
            model_name="show",
            name="title_ru",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=255,
                null=True,
                verbose_name="Translated title",
            ),
        ),
    ]
