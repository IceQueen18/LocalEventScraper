import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.minneapolisparks.org/event-calendar/list/'

try: 
    #sending the get request and adding a timeout for exception
    #200 means it is okay, 201 Creates, 401 unathorized, 
    #400 Bad request, 403 Forbidden
    #404 Not Found, 500 Internal Server Error.

    response = requests.get(url, timeout=3)

    # This will raise an exception for bad HTTP status codes
    response.raise_for_status()
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.ConnectionError:
    print("Network error connection occured")
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occured: {err}")
except requests.exceptions.RequestException as err:
    print(f"Unexpected error occured: {err}")

#getting status code and response
print("Status code: ", response.status_code)
#parsing reponse
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())
events = []
events_boxes = soup.find_all('div', class_='tribe-events-calendar-list__event-details')

for event in events_boxes:
    #getting the title, date, end time and location.

    details = {
        'title': event.find('a', class_="tribe-events-calendar-list__event-title-link"),
        'date' : event.find('span', class_="tribe-event-date-start"),
        'time' : event.find('span', class_="tribe-event-time"),
        'venue' : event.find('span', class_="tribe-events-calendar-list__event-venue-title"),
        'location' : event.find('span', class_="tribe-events-calendar-list__event-venue-address")
    }

    for key, value in details.items():
        if value:
            details[key] = value.get_text(strip=True)
            print(details[key])
             
        else:
            title_name = details.get('title', 'unknown')
            print(f"No {key} for {title_name} was found")

    #Checking if the time in the event does not exist
    # time_element = event.find('span', class_="tribe-event-time")
    # if time_element:
        # details['time'] = event.find('span', class_="tribe-event-time").get_text(strip=True)
    # else:
        # details['time'] = ''
        # print(f"No time for {details['title']} was found.")    

    # venue_element = event.find('span', class_="tribe-events-calendar-list__event-venue-title")
    # if venue_element:
        # details['venue'] = event.find('span', class_="tribe-events-calendar-list__event-venue-title").get_text(strip=True)
    # else:
        # details['venue'] = ''
        # print(f"No venue name for {details['title']} was found.")

    # location_element = event.find('span', class_="tribe-events-calendar-list__event-venue-address")
    # if location_element:
        # details['location'] = event.find('span', class_="tribe-events-calendar-list__event-venue-address").get_text(strip=True)
    # else:
        # details['location'] = ''
        # print(f"No location for {details['location']} was found.")
    
    # print(details)





print(f"Found events: {len(events_boxes)}")

