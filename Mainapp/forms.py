from django import forms 

from .models import Topic 

#we are using meta class because we already have a modelform 
#we dont have to redefine every time 

class TopicForm(forms.ModelForm):
    class Mata:
        model = Topic 
        fields = ["text"]
        labels = {"text":""}