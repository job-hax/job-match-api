from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StageSerializer 
from .models import Stage
import json
from .stage_stat import accept_rate, longest_dur, most_fail_stage

class StageAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)

class StageList(APIView):
    def get(self, request):
        model = Stage.objects.all()
        serializer = StageSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StageLocal(APIView):
    def get(self, request):
        with open('stages/date_data.json', 'r') as f:
            data = f.readlines()
        return Response(data)

class StageStat(APIView):
    def get(self, request):
        with open('stages/date_data.json', 'r') as json_file:
            data = [json.loads(x) for x in json_file.readlines()]
        
        res = {
            'accept_rate': accept_rate(data), 
            'longest_duration': longest_dur(data),
            'most_fail_stage': most_fail_stage(data),
        }
        return Response(res)
