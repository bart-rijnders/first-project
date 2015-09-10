import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

from datetime import datetime
from datetime import date as date
from datetime import timedelta as delta


try:
    import argparse
    Flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    Flags = None
except:
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

def Convert_Colour(col):
    return {            #cheapass switch statement
        'none' : None,
        'blue' : 1,
        'green' : 2,
        'purple' : 3,
        'red' : 4,
        'yellow' : 5,
        'orange' : 6,
        'turquoise' : 7,
        'gray' : 8,
        'bold blue' : 9,
        'bold green' : 10,
        'bold red' : 11
        }.get(str(col).lower(), None)


def get_UpcomingEvents(start ,stop, colour):
    credentials = get_Credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    if stop <= start:
        start = 0
        stop = 1

    now = datetime.combine(date.today() + delta(days=start), datetime.min.time()).isoformat() + 'Z'
    tomorrow = datetime.combine(date.today() + delta(days=stop), datetime.min.time()).isoformat() + 'Z'

    eventResult = service.events().list(calendarId='primary', timeMin=now, timeMax=tomorrow).execute()
    events = eventResult.get('items',[])

    if not events:
        return False
    else:
        colorCode = Convert_Colour(colour)
        for i in events:
            if dict(i).get('colorId', None) == colorCode:
                return True
        else:
            return False