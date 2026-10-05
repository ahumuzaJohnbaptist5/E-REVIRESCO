from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet)
router.register(r'submissions', views.SubmissionViewSet)
router.register(r'collections', views.CollectionRequestViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'assessments', views.AssessmentViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/submit/', views.submit_e_waste, name='submit_e_waste'),
    path('api/track/', views.track_e_waste, name='track_e_waste'),
    path('api/', include(router.urls)),
]