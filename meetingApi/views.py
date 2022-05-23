from django.http import JsonResponse
from .models import Meetings
from .serializers import MeetingSerializerGet,MeetingSerializerPost, MeetingSerializerPut
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer






@api_view(['GET','POST'])
def meeting_list(request):
    permission_classes = (IsAuthenticated,)
    if request.method == 'POST':
        # receiving post request
        serializer = MeetingSerializerPost(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    meetings = Meetings.objects.all()
    serializer = MeetingSerializerGet(meetings, many=True)
    return JsonResponse({'response': serializer.data})

@api_view(['GET','PUT','DELETE'])
def users_meeting(request,uid):
   
    try:
        # checking uid validity
        user_meetings = Meetings.objects.filter(user_id=uid)
    except Meetings.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)
 
 
    if request.method == 'GET':
          # getting all meetings for one user
        serializer = MeetingSerializerGet(user_meetings, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT'])
def users_meeting_update(request,meetingid,uid):
   
    try:
        print(f"user{uid} meeting{meetingid}")
        user_meeting = Meetings.objects.filter(user_id=uid,pk=meetingid) 
        # print("-"*100)
        # print(user_meeting)
        # print("-"*100)
        # return JsonResponse(MeetingSerializerGet(user_meeting, many=True).data, safe=False)
    except Meetings.DoesNotExist:
          return Response(status=status.HTTP_404_NOT_FOUND)
 
    
    if request.method == 'GET':
        return JsonResponse(MeetingSerializerGet(user_meeting, many=True).data, safe=False)

    elif request.method == 'PUT':
          # updatting meeting details
        # request.data["user_id"]=uid
        serializer = MeetingSerializerPut(user_meeting.first(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    # elif request.method == 'DELETE':
    #       # deleting meeting
    #     pass
    