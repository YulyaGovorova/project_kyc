# Generated by Django 5.0.4 on 2024-04-16 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0005_alter_documentstatus_options_customnotification'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
        migrations.AlterModelOptions(
            name='documentstatuschange',
            options={'verbose_name': 'Изменен статус документа', 'verbose_name_plural': 'Изменены статусы документов'},
        ),
    ]
