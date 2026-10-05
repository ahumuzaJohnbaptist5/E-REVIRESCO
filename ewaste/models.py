from django.db import models
import random
import string

def generate_tracking_id():
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"ER-2026-{random_str}"

class Customer(models.Model):
    CUSTOMER_TYPES = [('Individual', 'Individual'), ('Business', 'Business'), ('Institution', 'Institution')]
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    customer_type = models.CharField(max_length=20, choices=CUSTOMER_TYPES, default='Individual')
    
    def __str__(self): return self.name

class Submission(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='submissions')
    date_submitted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Registered")
    
    def __str__(self): return f"Submission {self.id} by {self.customer.name}"

class Item(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='items')
    tracking_id = models.CharField(max_length=20, unique=True, default=generate_tracking_id, editable=False)
    device_type = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    data_bearing = models.BooleanField(default=False)
    
    def __str__(self): return f"{self.tracking_id} - {self.device_type}"

class Assessment(models.Model):
    CATEGORIES = [
        ('A', 'A: Reuse'), ('B', 'B: Repair'), ('C', 'C: Refurbishment'),
        ('D', 'D: Component Recovery'), ('E', 'E: Recycling'), ('F', 'F: Specialist Disposal')
    ]
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='assessments')
    category = models.CharField(max_length=2, choices=CATEGORIES)
    notes = models.TextField(blank=True)
    assessed_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): return f"Assessment for {self.item.tracking_id}"

class CollectionRequest(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    requested_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")
    
    def __str__(self): return f"Collection for {self.customer.name} at {self.location}"