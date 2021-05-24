# Django Zoom Meetings


## Python package for creating and deleting zoom meetings
This package allows for easy scheduling and updating of Zoom meetings within your django app.


## installation
```python
pip install django-zoom-meetings
```

## Add django-zoom-meeting to your list of installed apps 

## Creating a meeting
```python
from django_zoom_meetings import ZoomMeetings
# Creat a JWT app your account https://marketplace.zoom.us/ and use
# the api_key, secret_key and your zoom email address to create a ZoomMeetings instance
my_zoom = ZoomMeetings(api_key,secret_key,zoom_email)

# required parameters are date,topic,duration and the password of the meeting 
create_meeting = my_zoom.CreateMeeting(date,str_topic,str_meeting_duration,str_meeting_password)
```

## Delete a meeting
```python
# to delete a meeting simply pass the meeting id as a string with no spaces
from django-zoom-meetings import ZoomMeetings
my_zoom = ZoomMeetings(api_key,secret_key,zoom_email)
delete_meeting = my_zoom.DeleteMeeting(str_meeting_id)
```
