from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Meetings

class MeetingSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Meetings
        fields = ['id','meeting_title','time_posted','meeting_minutes','file_url']

class MeetingSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Meetings
        fields = ['meeting_title', 'meeting_minutes','user_id','file_url']

class MeetingSerializerPut(serializers.ModelSerializer):
    class Meta:
        model = Meetings
        fields = [  'meeting_minutes','file_url']