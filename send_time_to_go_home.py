
from datetime import datetime
from pync import Notifier
from pprint import pprint
import googlemaps
import json
import os

DEPARTURE_POINT = '2F LaunchPad, corner Streets, Sheridan, Mandaluyong, Metro Manila'
ARRIVAL_POINT = 'SM Megamall, Epifanio de los Santos Ave, Ortigas Center, Mandaluyong, Metro Manila'
MAPS_LINK = 'https://www.google.com.ph/maps/dir/2F+LaunchPad,+corner+Streets,+Sheridan,+Mandaluyong,' + \
            '+Metro+Manila/SM+Megamall,+Epifanio+de+los+Santos+Avenue,+Mandaluyong/@14.579816,121.0488233' + \
            ',16z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x3397c843d548c681:0x45ee89aca3b50cea!2m2!1d121.' + \
            '0535383!2d14.5741085!1m5!1m1!1s0x3397c815ec1c52e7:0x49e80caaf287652b!2m2!1d121.0564561!' + \
            '2d14.583439?hl=en'

date_now = datetime.now()

with open('credentials.json') as json_file:
    json_dict = json.load(json_file)

google_client = googlemaps.Client(key=json_dict['google_key'])

# noinspection PyUnresolvedReferences
results = google_client.directions(DEPARTURE_POINT, ARRIVAL_POINT, mode='driving', departure_time=date_now)

#pprint(results)

time_before_arrival = results[0]['legs'][0]['duration_in_traffic']['text']

Notifier.notify(time_before_arrival, title='Traffic Status', open=MAPS_LINK)
print 'hhaha'
Notifier.remove(os.getpid())
print '-----'
#Notifier.list(os.getpid())

exit()