from rest_framework import serializers
from .models import *

class MediationSerializers(serializers.ModelSerializer):
    class Meta:
        model = MediaitonProfile
        fields = "__all__"

class MoringSongSerializers(serializers.ModelSerializer):
    class Meta:
        model =MoringSong
        fields ="__all__"

class RelaxSongSerializers(serializers.ModelSerializer):
    class Meta:
        model = RelaxSong
        fields ="__all__"

class SleepSongSerializers(serializers.ModelSerializer):
    class Meta:
        model = SleepSong
        fields ="__all__"