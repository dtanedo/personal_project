
from datetime import datetime
from selenium import webdriver
from twilio.rest import Client
import googlemaps
import json

date_now = datetime.now()

with open('credentials.json') as json_file:
    json_dict = json.load(json_file)

google_client = googlemaps.Client(key=json_dict['google_key'])

results = google_client.directions(json_dict['departure_point'], json_dict['arrival_point'],
                                   mode='driving', departure_time=date_now)

time_before_arrival = results[0]['legs'][0]['duration_in_traffic']['text']
print(time_before_arrival)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(json_dict['maps_link'])


client = Client(json_dict['account_sid'],
                json_dict['auth_token'])

message = client.messages.create(
    to=json_dict['receiving_number'],
    from_=json_dict['twilio_generated_number'],
    body='Mahal uwi nako in {}'.format(time_before_arrival))

if (message.sid):
    print('Sending of text message successful!')
