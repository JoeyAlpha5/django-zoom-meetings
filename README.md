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
from django-zoom-meetings import ZoomMeetings
my_zoom = ZoomMeetings(api_key,secret_key,zoom_email)
my_zoom.CreateMeeting(date,str_topic,str_meeting_duration,str_meeting_password)
```

## Delete a meeting
```python
from django-zoom-meetings import ZoomMeetings
my_zoom = ZoomMeetings(api_key,secret_key,zoom_email)
my_zoom.DeleteMeeting(str_meeting_id)
```

**Please note that the str_meeting_id must exclude spaces**
