from .models import Show
from .serializers import ShowSerializer

from rest_framework import viewsets
from rest_framework import permissions

class ShowViewSet(viewsets.ModelViewSet):
    """ API endpoint for shows"""
    queryset = Show.objects.all().order_by('-created_at')
    serializer_class = ShowSerializer
    # permission_classes = [permissions.IsAuthenticated]
