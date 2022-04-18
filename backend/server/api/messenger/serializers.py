from django.contrib.auth.models import User, Group
from api.messenger.models import UnreadMessage

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UnreadMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnreadMessage
        fields = ['sender_name', 'scraper_run_time']