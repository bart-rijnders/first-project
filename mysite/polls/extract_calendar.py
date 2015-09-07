import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime
from datetime import timedelta

try:
    import argparse
    Flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    Flags = None

Scopes = 'https://www.googleapis.com/auth/calendar.readonly'
Client_Secret = 'client_secret.json'
App_Name = 'MainClient'

def get_Credentials():
    homeDir = os.path.expanduser('~')
    credentialsDir = os.path.join(homeDir, '.credentials')
    if not os.path.exists(credentialsDir):
        os.makedirs(credentialsDir)
    credentialsPath = os.path.join(credentialsDir, 'MainClient.json')

    store = oauth2client.file.Storage(credentialsPath)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow= client.flow_from_clientsecrets(Client_Secret, Scopes)
        flow.user_agent = App_Name
        if Flags:
            credentials = tools.run_flow(flow, store, Flags)
    return credentials

def get_UpcomingEvents():
    credentials = get_Credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.date.today()
    tomorrow = now + timedelta(days=1)

    now = datetime.datetime.combine(now, datetime.datetime.min.time())
    tomorrow = datetime.datetime.combine(tomorrow, datetime.datetime.min.time())
    now = now.isoformat() + 'Z'
    tomorrow = tomorrow.isoformat() + 'Z'




    #eventResult = service.events().list(calendarId='primary', timeMin=now, maxResults=10, orderBy='startTime').execute()
    eventResult = service.events().list(calendarId='primary', timeMin=now, timeMax=tomorrow).execute()
    events = eventResult.get('items',[])

    if not events:
        return False
    else:
        return True
