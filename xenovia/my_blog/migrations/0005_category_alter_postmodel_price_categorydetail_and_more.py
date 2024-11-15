# Generated by Django 4.2 on 2024-11-06 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0004_alter_postmodel_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.CreateModel(
            name='CategoryDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('category', models.ManyToManyField(to='my_blog.category')),
            ],
        ),
        migrations.AddField(
            model_name='postmodel',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='my_blog.category'),
        ),
    ]
