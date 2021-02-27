# Generated by Django 3.1.7 on 2021-02-27 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predication',
            name='field_id',
            field=models.AutoField(db_column='_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='predication',
            name='id_langue',
            field=models.ForeignKey(db_column='id_langue', on_delete=django.db.models.deletion.CASCADE, to='app.langue'),
        ),
        migrations.AlterField(
            model_name='verset',
            name='field_id',
            field=models.AutoField(db_column='_id', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='verset',
            name='id_langue',
            field=models.ForeignKey(db_column='id_langue', on_delete=django.db.models.deletion.CASCADE, to='app.langue'),
        ),
        migrations.AlterField(
            model_name='verset',
            name='id_pred',
            field=models.ForeignKey(db_column='id_pred', on_delete=django.db.models.deletion.CASCADE, related_name='pred_verset', to='app.predication'),
        ),
    ]
