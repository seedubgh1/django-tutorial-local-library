# Generated by Django 4.2.2 on 2023-06-14 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_language_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='imprint',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
