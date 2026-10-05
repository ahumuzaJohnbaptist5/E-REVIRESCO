from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from rest_framework import viewsets
import json

from .models import Customer, Submission, CollectionRequest, Item, Assessment
from .serializers import (
    CustomerSerializer, SubmissionSerializer, 
    CollectionRequestSerializer, ItemSerializer, AssessmentSerializer
)

# --- FRONTEND & FORM API VIEWS ---

def home(request):
    return render(request, 'index.html')

@csrf_exempt
@require_POST
def submit_e_waste(request):
    try:
        data = json.loads(request.body)
        
        # 1. Create or get the Customer
        customer, created = Customer.objects.get_or_create(
            name=data.get('submitter_name'),
            contact_info=data.get('contact_info'),
            defaults={'customer_type': 'Individual'}
        )
        
        # 2. Create the Submission
        submission = Submission.objects.create(
            customer=customer,
            status="Registered - Awaiting Assessment"
        )
        
        # 3. Create the Item (The actual device)
        item = Item.objects.create(
            submission=submission,
            device_type=data.get('device_type'),
            condition=data.get('condition'),
            data_bearing=True # Defaulting to true for safety
        )
        
        return JsonResponse({
            'status': 'success',
            'tracking_id': item.tracking_id
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@require_GET
def track_e_waste(request):
    tracking_id = request.GET.get('tracking_id', '').strip().upper()
    
    if not tracking_id:
        return JsonResponse({'status': 'error', 'message': 'No tracking ID provided'}, status=400)

    try:
        item = Item.objects.get(tracking_id=tracking_id)
        return JsonResponse({
            'status': 'success',
            'data': {
                'tracking_id': item.tracking_id,
                'device_type': item.device_type,
                'condition': item.condition,
                'current_status': item.submission.status,
                'data_sanitized': False # Will update this later in the admin panel
            }
        })
    except Item.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'No record found'}, status=404)

# --- REST API VIEWSETS ---

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all().order_by('-date_submitted')
    serializer_class = SubmissionSerializer

class CollectionRequestViewSet(viewsets.ModelViewSet):
    queryset = CollectionRequest.objects.all()
    serializer_class = CollectionRequestSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer