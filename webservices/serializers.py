from django.contrib.auth.models import User, Group
from rest_framework import serializers
from webservices.models import *

class SongSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Group model """
    class Meta:
        model = Song
        fields='__all__'

class PodcastSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Group model """
    class Meta:
        model = Podcast
        fields='__all__'

class PodcastSerializer(serializers.ModelSerializer):
    """ Serializer to represent the Group model """
    class Meta:
        model = Podcast
        fields='__all__'
