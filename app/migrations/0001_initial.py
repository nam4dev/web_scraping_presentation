# Generated by Django 2.2.2 on 2019-06-18 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512, unique=True)),
                ('page_link', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='PullRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=512)),
                ('link', models.URLField(max_length=512)),
                ('status', models.CharField(choices=[('is_open', 'Open'), ('is_closed', 'Closed'), ('is_unknown', 'Unknown')], default='is_unknown', max_length=10)),
                ('scrapped_uri', models.URLField(max_length=512)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pull_requests', to='app.Author')),
            ],
        ),
    ]
