import requests
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Windows/System32/chromedriver_win32/chromedriver.exe")

url = "https://api.github.com/users/avielb/repos"
driver.get(url)

def check_repo():
    ping = requests.get(url)
    data = ping.json()
    repo_list = []
    if ping.status_code == 200:
        for i in range(5):
            tempRepo = driver.find_element(by=id, value="name")
            repo_list.insert(i, tempRepo)
    print(repo_list)

check_repo()
