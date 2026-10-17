from django.contrib import admin
from .models import Customer, Submission, Item, Assessment, CollectionRequest

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_info', 'customer_type')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_submitted', 'status')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'device_type', 'condition', 'data_bearing', 'submission')

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('item', 'category', 'assessed_at')

@admin.register(CollectionRequest)
class CollectionRequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'location', 'requested_date', 'status')

from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_published', 'published_at', 'updated_at')
    list_filter = ('is_published', 'category')
    search_fields = ('title', 'summary', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)
    ordering = ('-created_at',)
