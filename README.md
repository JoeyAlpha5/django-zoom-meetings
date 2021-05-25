# Django Zoom Meetings


## Python package for creating and deleting zoom meetings
This package allows for easy scheduling and updating of Zoom meetings within your django app.

##### Creat a JWT app on your Zoom account https://marketplace.zoom.us/ and use
##### the api_key, secret_key and your zoom email address to create a ZoomMeetings instance


## installation
```python
pip install django-zoom-meetings
```

## Creating a meeting
```python
from django_zoom_meetings import ZoomMeetings
# Creat a JWT app your account https://marketplace.zoom.us/ and use
# the api_key, secret_key and your zoom email address to create a ZoomMeetings instance
my_zoom = ZoomMeetings(api_key,secret_key,zoom_email)

# required parameters are date,topic,duration and the password of the meeting. In return you will get all the meeting details including the join url
create_meeting = my_zoom.CreateMeeting(date,str_topic,str_meeting_duration,str_meeting_password)
```


## Get meeting details
```python
# to retrieve meeting details from your Zoom account simply pass the meeting id as a string with no spaces
from django_zoom_meetings import ZoomMeetings
my_zoom = ZoomMeetings(api_key,secret_key,zoom_email)
get_meeting = my_zoom.GetMeeting(str_meeting_id)
```

## Delete a meeting
```python
# to delete a meeting simply pass the meeting id as a string with no spaces
from django_zoom_meetings import ZoomMeetings
my_zoom = ZoomMeetings(api_key,secret_key,zoom_email)
delete_meeting = my_zoom.DeleteMeeting(str_meeting_id)
```
