from django.contrib.auth.models import User, Group
from api.messenger.models import UnreadMessage
from api.messenger.models import UnreadMessage
from rest_framework import viewsets, permissions
from api.messenger.serializers import UserSerializer, GroupSerializer, UnreadMessageSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UnreadMessageViewSet(viewsets.ModelViewSet):
    queryset = UnreadMessage.objects.all()
    serializer_class = UnreadMessageSerializer
