# Generated by Django 4.2.11 on 2025-02-20 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0003_delete_qualifiedmark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='student',
            name='normalized_marks',
            field=models.FloatField(default=0),
        ),
    ]
