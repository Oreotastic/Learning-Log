# Generated by Django 2.2.7 on 2019-11-21 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_thisisatest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thisisatest',
            old_name='food',
            new_name='test',
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodDesc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_logs.ThisIsATest')),
            ],
        ),
    ]
