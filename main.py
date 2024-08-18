import requests
from bs4 import BeautifulSoup


class Job:
    def __init__(self, url, company, location, salary) -> None:
        self.url = url
        self.company = company
        self.location = location
        self.salary = salary

    def __str__(self) -> str:
        return f"URL: {self.url}\nCompany: {self.company}\nLocation: {self.location}\nSalary:{self.salary}\n"


keywords = ["flutter", "python", "golang"]
all_jobs = []
for keyword in keywords:
    response = requests.get(
        f"https://remoteok.com/remote-{keyword}-jobs",
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
        },
    )
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find_all("tr", class_="job")

    keyword_jobs = []
    for job in jobs:
        url = f"https://remoteok.com{job['data-url']}"
        company = job["data-company"]
        try:
            location = job.find("div", class_="tooltip").text
        except AttributeError:
            location = "Unknown"
        try:
            salary = job.find("div", class_="tooltip-set").text
        except AttributeError:
            salary = "Unknown"
        keyword_jobs.append(Job(url, company, location, salary))
    all_jobs.append({keyword: keyword_jobs})

for d in all_jobs:
    for key, value in d.items():
        print(f"================={key}=================")
        for job in value:
            print(job)
