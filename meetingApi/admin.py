import imp
from re import I
from django.contrib import admin
from .models import Meetings

# registering model for admin view
admin.site.register(Meetings)