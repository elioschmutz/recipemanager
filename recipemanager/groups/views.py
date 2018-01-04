from .serializers import GroupSerializer
from django.contrib.auth.models import Group
from rest_framework import permissions
from rest_framework import viewsets


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (permissions.IsAdminUser, )

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
