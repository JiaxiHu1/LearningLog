from django import forms 

from .models import Entry, Topic 

#we are using meta class because we already have a modelform 
#we dont have to redefine every time 

class TopicForm(forms.ModelForm):
    class Mata: #sub model 
        #this is the template below 
        model = Topic 
        fields = ["text"]
        labels = {"text":""}

class EntryForm(forms.ModelForm):
    class Mata: #sub model 
        #this is the template below 
        model = Entry
        fields = ["text"]
        labels = {"text":""}
        widgets = {'text':forms.Textarea(attrs={'cols':80})} #modifying the model of the look, 80 columns 
#three steps 
#forms 
#new urls
#new views
#tempalte 