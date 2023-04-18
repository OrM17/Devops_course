import datetime
import requests
def check_if_url(url):
    response = requests.get(url)
    if 200 <= response.status_code < 300:
        return True
    return False

print(check_if_url("https://sport5.co.il"))


