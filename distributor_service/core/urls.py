from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DistributorViewSet, PaymentViewSet
from .views import cashfree_webhook

router = DefaultRouter()
router.register(r'distributors', DistributorViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cashfree/webhook/', cashfree_webhook, name='cashfree_webhook'),

]
