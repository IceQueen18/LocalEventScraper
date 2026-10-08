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
events_boxes = soup.find('div', class_='tribe-events-calendar-list__event-details')

print(f"Found events: {len(events_boxes)}")

