# Generated by Django 4.0.3 on 2022-04-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobs',
            options={'verbose_name': 'Job', 'verbose_name_plural': 'Jobs'},
        ),
        migrations.AlterModelOptions(
            name='referencias',
            options={'verbose_name': 'Referencia', 'verbose_name_plural': 'Referencias'},
        ),
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(default='C', max_length=2),
        ),
    ]