# Generated by Django 4.1.3 on 2022-11-16 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'Two'), (3, 'Three')], default=1),
        ),
        migrations.AddField(
            model_name='contractwithpartner',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'Two'), (3, 'Three')], default=1),
        ),
        migrations.AlterField(
            model_name='contractimage',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts_images', to='contracts.contract'),
        ),
    ]