from django.contrib import admin
from .models import Job
# Register your models here.

admin.site.register(Job)

# Tells the admin about new model named Job, and this causes Job to show up in admin panel
