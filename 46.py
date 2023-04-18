import requests
from requests.exceptions import InvalidURL


try:
    response = requests.get("fdsdf")
except InvalidURL:
    print("invalid url was insert")