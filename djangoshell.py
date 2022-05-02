import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django 
django.setup()


from Mainapp.models import Topic 

topics = Topic.objects.all() #all objects - chess and rock climbing 


for t in topics: #print out all the objects 
    print(t.id,'  ', t) #string method - so when we refer to t it will give the whole thing
    #when we define the string method - when you call it it will return to the text 
    #def __str__(self): return self.text - so the return will be the text - it's in the models.py


t = Topic.objects.get(id=1) #get is for when you know the specific id 
print(t.text)
print(t.data_added)

#for all topics 
entries = t.entry_set.all()

for e in entries:
    print(e) #will print out the first 50 characters because that's how we defined it 
