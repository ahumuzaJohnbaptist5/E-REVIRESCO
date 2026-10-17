# Generated manually for the public E-REVIRESCO articles feature.
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ewaste', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=220, unique=True)),
                ('category', models.CharField(default='E-Waste Awareness', max_length=80)),
                ('summary', models.CharField(max_length=320)),
                ('content', models.TextField(help_text='Article body. Separate paragraphs with blank lines.')),
                ('author', models.CharField(blank=True, default='E-REVIRESCO Team', max_length=100)),
                ('is_published', models.BooleanField(default=False)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-published_at', '-created_at'],
            },
        ),
    ]
