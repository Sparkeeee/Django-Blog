# Generated by Django 4.2.10 on 2024-02-27 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='field_2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='field_3',
        ),
    ]