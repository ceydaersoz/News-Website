# Generated by Django 4.1.3 on 2024-01-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0003_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
