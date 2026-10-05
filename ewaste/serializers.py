from rest_framework import serializers
from .models import Customer, Submission, CollectionRequest, Item, Assessment

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:
        model = Submission
        fields = '__all__'

class CollectionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionRequest
        fields = '__all__'