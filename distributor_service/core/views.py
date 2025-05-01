from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Distributor, Payment
from .serializers import DistributorSerializer, PaymentSerializer
from .utils.sap import sync_distributor_to_sap
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Payment

@api_view(['POST'])
@permission_classes([AllowAny])  # Secure with a secret token in production
def cashfree_webhook(request):
    tx_id = request.data.get("transaction_id")
    status = request.data.get("transaction_status")

    try:
        payment = Payment.objects.get(transaction_id=tx_id)
        payment.status = status.upper()  # Example: SUCCESS
        payment.save()
        return Response({"message": "Payment status updated"}, status=200)
    except Payment.DoesNotExist:
        return Response({"error": "Payment not found"}, status=404)

class DistributorViewSet(viewsets.ModelViewSet):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        distributor = serializer.save()
        sync_distributor_to_sap(distributor)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
