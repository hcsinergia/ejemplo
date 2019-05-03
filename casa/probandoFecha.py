
import csv
from datetime import datetime


def parseISO8601DateTime(datetimeStr):
    import time
    from datetime import datetime, timedelta

    def log_date_string(when):
        gmt = time.gmtime(when)
        if time.daylight and gmt[8]:
            tz = time.altzone
        else:
            tz = time.timezone
        if tz > 0:
            neg = 1
        else:
            neg = 0
            tz = -tz
        h, rem = divmod(tz, 3600)
        m, rem = divmod(rem, 60)
        if neg:
            offset = '-%02d%02d' % (h, m)
        else:
            offset = '+%02d%02d' % (h, m)
    
        return time.strftime('%d/%b/%Y:%H:%M:%S ', gmt) + offset
    
    dt = datetime.strptime(datetimeStr, '%Y-%m-%dT%H:%M:%S.%fZ')
    timestamp = dt.timestamp()
    return dt + timedelta(hours=dt.hour-time.gmtime(timestamp).tm_hour)

def ConvertirFecha(datetimeStr):
    import time
    from datetime import datetime, timedelta

    def log_date_string(cadena, when):
        gmt = time.gmtime(when)
        
        return time.strftime('%d/%b/%Y:%H:%M:%S ', gmt) + offset
    
    dt = datetime.strptime(datetimeStr, '%Y-%m-%dT%H:%M:%S.%fZ')
    timestamp = dt.timestamp()
    return dt + timedelta(hours=dt.hour-time.gmtime(timestamp).tm_hour)


import csv
f = open('fh2.csv')

lines = csv.reader(f,delimiter=';')
COUNT = 0
for line in lines:
    print(str(line[0]), str(line[1]), str(line[2]), str(line[3]))
    print(str(line[2]))
    inicio = ConvertirFecha(str(line[2]))
    print(inicio.hours)