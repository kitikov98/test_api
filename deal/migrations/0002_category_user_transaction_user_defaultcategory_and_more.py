# Generated by Django 4.1.3 on 2022-11-05 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DefaultCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('def_cat', models.CharField(choices=[('Забота о себе', 'Забота о себе'), ('Зарплата', 'Зарплата'), ('Здоровье и фитнес', 'Здоровье и фитнес'), ('Кафе и рестораны', 'Кафе и рестораны'), ('Машина', 'Машина'), ('Образование', 'Образование'), ('Отдых и развлечения', 'Отдых и развлечения'), ('Платежи, комиссии', 'Платежи, комиссии'), ('Покупки: одежда, техника', 'Покупки: одежда, техника'), ('Продукты', 'Продукты'), ('Проезд', 'Проезд')], max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='deal.defaultcategory'),
        ),
    ]