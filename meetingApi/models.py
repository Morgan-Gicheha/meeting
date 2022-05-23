from django.db import models
from .utilities import time_now


class Meetings(models.Model):
    '''This class is a represenation of the meetings database'''
    meeting_title = models.CharField(max_length=200,blank=False)
    time_posted = 	models.CharField(max_length=30 , default=time_now())
    user_id = models.IntegerField(blank=False)
    file_url = models.CharField(max_length=250,blank=True, default='')
    meeting_minutes = models.TextField(blank=True, default='')

    # changing the representation of the object 
    def __str__(self) -> str:
        return self.meeting_title + ' - '+ str(self.pk) + '-' + str(self.time_posted)


