# Generated by Django 4.0.4 on 2022-05-31 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newssite', '0004_createpost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='createPost',
            new_name='createPostModel',
        ),
        migrations.RenameField(
            model_name='createpostmodel',
            old_name='description',
            new_name='body',
        ),
    ]
