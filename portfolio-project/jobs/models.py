from django.db import models

class Job(models.Model):
  
  image = models.ImageField(upload_to='images/')
  summary = models.CharField(max_length=200)

# Should return string in /admin console
  #def __str__(self):
       #return str(self.summary)
  
#https://stackoverflow.com/questions/11871221/python-typeerror-str-returned-non-string-but-still-prints-to-output
