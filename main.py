import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(
    response.content,
    "html.parser",
)

jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

for job in jobs:
    title = job.find("span", class_="title").text
    try:
        region = job.find("span", class_="region").text
    except AttributeError:
        region = "No Region"

    try:
        company, position, _ = job.find_all("span", class_="company")
    except ValueError:
        company, position = job.find_all("span", class_="company")

    company = company.text
    position = position.text
    print(title, company, position, region, "----------\n")
