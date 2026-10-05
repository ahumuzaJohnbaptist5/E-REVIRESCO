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