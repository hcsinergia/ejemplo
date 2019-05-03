from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

##https://developers.google.com/calendar/v3/reference/events
##Doc fecha y hora internacional
##https://tools.ietf.org/html/rfc3339
##https://es.wikipedia.org/wiki/ISO_8601

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

##GMT_OFF = '-07:00' #argentina -3
##TIMEZONE = 'America/Argentina/Buenos_Aires'



#Leer CSV
#http://josearcosaneas.github.io/python/xls/csv/2016/12/26/leer-excel-csv.html
import csv
f = open('fh2.csv')
#lines = csv.reader(f)
#Cambiar el tipo de separador a ; ,
lines = csv.reader(f,delimiter=';')
for line in lines:
    #print(str(line[0]), str(line[1]), str(line[2]), str(line[3]))
     #print(str(line[0]))
    event1 = {
        'summary': str(line[0]),
        'location': str(line[1]),
        'start': {
            #'dateTime': '2018-12-21T09:00:00-07:00',
            'dateTime': line[2],
            'timeZone' : 'America/Argentina/Buenos_Aires',
        },
        'end': {
            'dateTime': line[3],
            'timeZone' : 'America/Argentina/Buenos_Aires',
        },   
        #cada dos dias
        # 'recurrence' : [
        #     'RRULE:FREQ=DAILY;COUNT=2' 
        # ],
        'reminders':{
            'useDefault': False,
            'overrides': [
                {'method' : 'email', 'minutes': 24 * 60},
                {'method' : 'popup', 'minutes' : 10},
            ],
        },
    }

    print(event1)
    event1 = service.events().insert(calendarId='primary', body=event1).execute()
    #print('Event created: %s' % (event1.get('htmlLink')))

