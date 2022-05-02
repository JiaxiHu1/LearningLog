from django.urls import path

from . import views 

app_name = "Mainapp"

urlpatterns = [
    path("",views.index, name="index"),
    path("topics",views.topics, name="topics"),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/',views.new_topic, name='new_topic'),
    

]

#this is for the learning log app 
#when we load a page - topics - then we want to get into the individual topics - load different topics 
#create id for each individual topics - the third line 

