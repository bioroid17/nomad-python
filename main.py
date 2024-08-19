from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv


class WantedScraper:
    def __init__(self, keyword):
        self.jobs_db = []
        self.keyword = keyword

    def get_content(self):
        p = sync_playwright().start()

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(f"https://www.wanted.co.kr/search?query={self.keyword}&tab=position")
        # time.sleep(5)

        # page.click("button.Aside_searchButton__rajGo")
        # time.sleep(5)

        # page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
        # time.sleep(5)

        # page.keyboard.down("Enter")
        # time.sleep(5)

        # page.click("a#search_tab_position")

        for x in range(5):
            time.sleep(5)
            page.keyboard.down("End")

        content = page.content()

        p.stop()

        return content

    def scrape(self):

        content = self.get_content()

        soup = BeautifulSoup(content, "html.parser")

        jobs = soup.find_all("div", class_="JobCard_container__REty8")

        jobs_db = []

        for job in jobs:
            link = f"https://www.wanted.co.kr{job.find('a')['href']}"
            title = job.find("strong", class_="JobCard_title__HBpZf").text
            company_name = job.find("span", class_="JobCard_companyName__N1YrF").text
            reward = job.find("span", class_="JobCard_reward__cNlG5").text

            j = {
                "title": title,
                "company_name": company_name,
                "reward": reward,
                "link": link,
            }
            jobs_db.append(j)

        file = open(f"{self.keyword}_jobs.csv", "w", encoding="utf-8-sig")
        writer = csv.writer(file)
        writer.writerow(
            [
                "Title",
                "Company",
                "Reward",
                "Link",
            ]
        )
        for job in jobs_db:
            writer.writerow(job.values())
        file.close()


keywords = [
    "python",
    "django",
    "nextjs",
    "flutter",
    "kotlin",
]

for keyword in keywords:
    scraper = WantedScraper(keyword)
    scraper.scrape()
