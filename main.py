from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_page_count(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # 브라우저 꺼짐 방지 코드

    # 크롬드라이버를 최신으로 유지해줍니다.
    browser = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    browser.get(f"{base_url}{keyword}")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.select_one("nav.css-jbuxu0.ecydgvn0")
    if pagination == None:
        return 1
    pages = pagination.find_all("div", recursive=False)
    print(len(pages))


get_page_count("python")


def extract_indeed_jobs(keyword):
    base_url = "https://kr.indeed.com/jobs?q="
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)  # 브라우저 꺼짐 방지 코드

    # 크롬드라이버를 최신으로 유지해줍니다.
    browser = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    browser.get(f"{base_url}{keyword}")

    results = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_list = soup.find("ul", class_="css-zu9cdh")
    jobs = job_list.find_all("li", recursive=False)
    for job in jobs:
        zone = job.find("div", class_="mosaic-zone")
        if zone == None:
            anchor = job.select_one("h2 a")
            title = anchor['aria-label']
            link = anchor['href']
            company = job.find("span", class_="companyName")
            location = job.find("div", class_="companyLocation")
            job_data = {
                "link": f"https://kr.indeed.com{link}",
                "company": company.string,
                "location": location.string,
                "position": title
            }
            results.append(job_data)
    for result in results:
        print(result, "\n//////////\n")
