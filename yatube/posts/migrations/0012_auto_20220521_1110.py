# Generated by Django 2.2.9 on 2022-05-21 01:10

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20220519_1031'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'author'), name='unique_follow'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(user=django.db.models.expressions.F('author')), name='dont_follow_self'),
        ),
        migrations.AlterModelTable(
            name='follow',
            table='posts_follow',
        ),
    ]