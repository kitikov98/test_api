# Generated by Django 4.1.3 on 2022-11-05 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0004_rename_def_cat_defaultcategory_cat_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='deal.defaultcategory'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]