# Generated by Django 4.2.10 on 2024-02-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='field_2',
            field=models.IntegerField(default=42),
        ),
        migrations.AddField(
            model_name='post',
            name='field_3',
            field=models.CharField(null=True),
        ),
    ]
