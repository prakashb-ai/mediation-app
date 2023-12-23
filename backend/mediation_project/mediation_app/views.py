from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def get_data_profile(request):
    profile = MediaitonProfile.objects.all()
    serializers = MediationSerializers(profile,many=True)
    return Response(serializers.data)


@api_view(['POST'])
def post_data_profile(request):
    serializers = MediationSerializers(data= request.data)
    if serializers.is_valid():
        serializers.save()
    
    return Response(serializers.data)

@api_view(['PUT'])
def update_profile(request,id):
    profile_upd = MediaitonProfile.objects.get(id=id)
    serializers = MediationSerializers(instance=profile_upd,data=request.data)
    if serializers.is_valid():
        serializers.save()
    
    return Response(serializers.data)

@api_view(['DELETE'])
def delete_profile(request,id):
    profile = MediaitonProfile.objects.get(id=id)
    profile.delete()
    return Response("data was deleted")


#for relax songs

@api_view(['GET'])
def get_relax_songs(request):
    relax_song = RelaxSong.objects.all()
    serializers = RelaxSongSerializers(relax_song,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def post_relax_song(request):
    serializers = RelaxSongSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['PUT'])
def update_relax_song(request,id):
    update_relax = RelaxSong.objects.get(id=id)
    serializers = RelaxSongSerializers(instance=update_relax,data=request.data)
    if serializers.is_valid():
        serializers.save()
    
    return Response(serializers.data)

@api_view(['DELETE'])
def delete_relax_song(request,id):
    delete_relax_song = RelaxSong.objects.get(id=id)
    delete_relax_song.delete()
    return Response("data was deleted")









    

