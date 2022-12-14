# Generated by Django 4.1.2 on 2022-11-27 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_makeup_foto_alter_pricheski_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zayavki',
            name='makeup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='content.makeup', verbose_name='Макияж'),
        ),
        migrations.AlterField(
            model_name='zayavki',
            name='pricheski',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='content.pricheski', verbose_name='Причёска'),
        ),
    ]
