# Generated by Django 4.2.2 on 2023-06-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_bookinstance_imprint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='imprint',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
