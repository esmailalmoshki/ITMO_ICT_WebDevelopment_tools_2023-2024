# Generated by Django 5.0.3 on 2024-03-28 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_book_member_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='member_id',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='booktaking',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RenameField(
            model_name='booktaking',
            old_name='member_id',
            new_name='member',
        ),
    ]
