import requests
import json

session = requests.Session()
login = session.get("https://getdesk.com/en/login")

datas = {
    'email': 'alina.zabaidulina.1990@gmail.com',
    'password': 'Gasprom1990'
}

response = session.post("https://getdesk.com/sign_in", data = datas).text


main_page = session.get("https://getdesk.com/")
coordinates = {
    "NELat": 55.88371520894671,
    "NELng": 49.38219465644529,
    "SWLat": 55.69183731690293,
    "SWLng": 48.86446394355467,
    }
search = session.get("https://getdesk.com/xhr/office/by_coordinates", json = coordinates)
office = session.get("https://getdesk.com/ru/office/61")

location_id = {"location_id":61,"begin":"2023-10-8T00:00:00","end":"2023-10-30T00:00:00"}

free_office = session.post("https://getdesk.com/xhr/free_office", json= location_id).text


space = {"booking_office_space_ids_count":[{"id":108,"count":1}],"booking_begin":"2023-10-20T00:00:00","booking_end":"2023-10-25T23:59:59","localtime":"2023-07-21T17:52:37"}

booking = session.post("https://getdesk.com/xhr/booking", json= space).text
print(booking)
#order_id = json.load(booking)["id"]
#print(order_id)
