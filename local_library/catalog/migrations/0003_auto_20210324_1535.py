# Generated by Django 3.1.7 on 2021-03-24 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_book_language'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back']},
        ),
        migrations.RenameField(
            model_name='bookinstance',
            old_name='due_book',
            new_name='due_back',
        ),
    ]
