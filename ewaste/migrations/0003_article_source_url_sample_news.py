from datetime import datetime, timezone

from django.db import migrations, models


def add_sample_news(apps, schema_editor):
    Article = apps.get_model('ewaste', 'Article')
    Article.objects.get_or_create(
        slug='snappy-dumpster-north-carolina-c-and-d-market',
        defaults={
            'title': 'Snappy Dumpster navigates North Carolina’s booming C&D market',
            'category': 'Waste Industry News',
            'summary': 'A profile of a small waste-hauling business in North Carolina, covering its growth, acquisition of another local hauler, and lessons about customer relationships and operating costs.',
            'content': (
                'Waste Dive reports on Snappy Dumpster Rental, a small hauling company operating in the Charlotte, North Carolina, area. The story describes how owner Ian Olmsted started the business while working another job and later acquired a fellow local hauler.\n\n'
                'The article highlights practical challenges for waste businesses, including the cost of trucks, fuel and landfill services, and the importance of retaining customers during a business transition. It also describes how local operators can compete by providing responsive, personal service.\n\n'
                'Why this may matter to waste-sector readers: the story offers an example of how local collection services develop and how customer trust, reliable logistics and operational costs influence waste-management businesses. This report focuses on construction and demolition waste, not electronic waste specifically.'
            ),
            'source_url': 'https://wastedive.com/news/snappy-dumpster-north-carolina-market-acquisition/832630/',
            'author': 'E-REVIRESCO Team (summary of Waste Dive reporting)',
            'is_published': True,
            'published_at': datetime(2026, 10, 16, 12, 0, tzinfo=timezone.utc),
        },
    )


def remove_sample_news(apps, schema_editor):
    Article = apps.get_model('ewaste', 'Article')
    Article.objects.filter(slug='snappy-dumpster-north-carolina-c-and-d-market').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('ewaste', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='source_url',
            field=models.URLField(blank=True, default='', help_text='Optional link to the original source or further reading.'),
        ),
        migrations.RunPython(add_sample_news, remove_sample_news),
    ]
