import jwt
import datetime
import requests
import json


class ZoomMeetings:
    def __init__(self,api_key,secret_key,user_email):
        self.time_now = datetime.datetime.now()
        self.expiration_time = self.time_now+datetime.timedelta(minutes=20)
        self.expiration_in_seconds = round(self.expiration_time.timestamp())
        # token requirements
        self.headers = {"alg": "HS256","typ": "JWT"}
        self.payload = {"iss": api_key,"exp": self.expiration_in_seconds}

        # generate token
        self.request_token = jwt.encode(self.payload,secret_key,algorithm="HS256",headers=self.headers)

        self.email = user_email

    def CreateMeeting(self,date,topic,meeting_duration,meeting_password):
        required_date_format = date.strftime("%Y-%m-%dT%H:%M:%SZ")
        url = 'https://api.zoom.us/v2/users/'+self.email+'/meetings'
        jsonObj = {"topic": topic, "start_time":required_date_format,"duration":meeting_duration,"password":meeting_password}
        header = {'authorization': 'Bearer '+self.request_token}
        zoom_create_meeting = requests.post(url,json=jsonObj, headers=header)
        return json.loads(zoom_create_meeting.text)

    def DeletMeeting(self,meeting_id):
        url = 'https://api.zoom.us/v2/meetings/'+str(meeting_id)
        header = {'authorization': 'Bearer '+self.request_token}
        zoom_delete_meeting = requests.delete(url, headers=header)
        return zoom_delete_meeting

    def GetMeeting(self,meeting_id):
        url = 'https://api.zoom.us/v2/meetings/'+str(meeting_id)
        header = {'authorization': 'Bearer '+self.request_token}
        get_zoom_meeting = requests.get(url, headers=header)
        return json.loads(get_zoom_meeting.text)

