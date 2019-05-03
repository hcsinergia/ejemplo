from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

#https://developers.google.com/calendar/v3/reference/events

try:
    import argparse
    flag=argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flag = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

#GMT_OFF = '-07:00'
#TIMEZONE = 'America/Argentina/Buenos_Aires'
event = {
    'summary':'Prueba Escribiendo Eventos Aldo',
    'location': 'Diag 74, 202, La Plata, Buenos Aires, Argentina',
    'start': {
        'dateTime': '2018-12-21T09:00:00-07:00',
        'timeZone' : 'America/Argentina/Buenos_Aires',
    },
    'end': {
        'dateTime': '2018-12-21T17:00:00-07:00',
        'timeZone' : 'America/Argentina/Buenos_Aires',
    },   
    #'start':  {'dateTime': '2018-12-20T19:00:00%s' % GMT_OFF},#'timeZone': TIMEZONE},
    #'end':    {'dateTime': '2018-12-20T22:00:00%s' % GMT_OFF},#'timeZone': TIMEZONE},
    'recurrence' : [
        'RRULE:FREQ=DAILY;COUNT=2' #cada dos dias
    ],
    # 'attendees': [
    #     {'email1' : 'hcsinergia@gmail.com'},
    # ],
    #'recurrence': ['RRULE:FREQ=MONTHLY;INTERVAL=2;UNTIL=20171231']
    'reminders':{
        'useDefault': False,
        'overrides': [
            {'method' : 'email', 'minutes': 24 * 60},
            {'method' : 'popup', 'minutes' : 10},
        ],
    },
}

event = service.events().insert(calendarId='primary', body=event).execute()
print('Event created: %s' % (event.get('htmlLink')))



