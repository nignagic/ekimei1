# Generated by Django 2.1 on 2019-12-04 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ekimei1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='name',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='part_name', to='ekimei1.Creator', verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='youtubechannel',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='channel', to='ekimei1.Creator', verbose_name='作者'),
        ),
    ]