# Generated by Django 4.1.4 on 2023-02-08 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0002_remove_list_date_remove_list_description_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={"ordering": ["date"]},
        ),
    ]
