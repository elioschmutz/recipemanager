from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import permissions
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.IsAdminUser, )

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
