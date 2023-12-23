from django.db import models

# Create your models here.

class MediaitonProfile(models.Model):
    username = models.CharField(max_length=50,blank=True)
    bio = models.CharField(max_length=50,blank=True)
    profile_image = models.ImageField(upload_to='profile_images/',blank=True)

    def __str__(self):
        return self.username


class SleepSong(models.Model):
    title = models.CharField(max_length=50,blank=True)
    album = models.CharField(max_length=50,blank=True)
    artist = models.CharField(max_length=50,blank=True)
    duration = models.DurationField()

    def __str__(self):
        return self.title
    
class MoringSong(models.Model):
    title = models.CharField(max_length=50,blank=True)
    album = models.CharField(max_length=50,blank=True)
    artist = models.CharField(max_length=50,blank=True)
    duration = models.DurationField()

    def __str__(self):
        return self.title

class RelaxSong(models.Model):
    title = models.CharField(max_length=50,blank=True)
    album = models.CharField(max_length=50,blank=True)
    artist = models.CharField(max_length=50,blank=True)
    duration = models.DurationField()

    def __str__(self):
        return self.title