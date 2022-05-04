from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Topic(models.Model):#inheritance 
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True) #this is the date that when we added the topic 

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self): #string method here. It returns back whatever you want to return. Actual information 
        return self.text #this will return name of the topic. Because the text is the information about the topic 
        

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    #we want entries to be this not "entrys"
    class Meta:
        verbose_name_plural = "entries"
        

    def __str__(self):
        #just the first 50 characters and then just ... after that 
        return f"{self.text[:50]}..."
