# Django Zoom Meetings


## Python package for creating and deleting zoom meetings
This package allows for easy scheduling and updating of Zoom meetings within your django app.


## installation
```
1.  pip install django-zoom-meetings
2. add django-zoom-meetings to your list of installed apps
```


## Creating a meeting
```
1. from django-zoom-meetings import ZoomMeetings
2. my_zoom = ZoomMeetings(api_key,secret_key,zoom_email)
3. my_zoom.CreateMeeting(date,str_topic,str_meeting_duration,str_meeting_password)
```

## Delete a meeting
```
1. from django-zoom-meetings import ZoomMeetings
2. my_zoom = ZoomMeetings(api_key,secret_key,zoom_email)
3. my_zoom.DeleteMeeting(str_meeting_id)

**Please note that the str_meeting_id must exclude spaces**
```