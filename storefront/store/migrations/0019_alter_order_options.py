# Generated by Django 4.1.1 on 2022-09-18 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0018_alter_customer_options_remove_customer_email_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="order",
            options={"permissions": [("cancel_order", "Can cancel order")]},
        ),
    ]
