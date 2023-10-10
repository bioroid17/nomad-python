from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # 브라우저 꺼짐 방지 코드

# 크롬드라이버를 최신으로 유지해줍니다.
browser = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)
browser.get(f"{base_url}{search_term}")

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="css-zu9cdh")
jobs = job_list.find_all("li", recursive=False)
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        print("job li")
    else:
        print("mosaic li")
