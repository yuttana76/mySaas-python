# Generated by Django 5.2 on 2025-04-25 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("subscriptions", "0002_subscription_subscription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="Subscription",
            field=models.ManyToManyField(
                limit_choices_to={
                    "codename__in": ["advanced", "pro", "basic", "basic_ai"],
                    "content_type__app_label": "subscriptions",
                },
                to="auth.permission",
            ),
        ),
    ]
