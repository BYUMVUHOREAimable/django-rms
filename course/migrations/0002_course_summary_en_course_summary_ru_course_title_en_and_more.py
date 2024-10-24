# Generated by Django 4.2.16 on 2024-09-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="summary_en",
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="course",
            name="summary_ru",
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="course",
            name="title_en",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="course",
            name="title_ru",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="program",
            name="summary_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="program",
            name="summary_ru",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="program",
            name="title_en",
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="program",
            name="title_ru",
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="upload",
            name="title_en",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="upload",
            name="title_ru",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="uploadvideo",
            name="summary_en",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="uploadvideo",
            name="summary_ru",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="uploadvideo",
            name="title_en",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="uploadvideo",
            name="title_ru",
            field=models.CharField(max_length=100, null=True),
        ),
    ]