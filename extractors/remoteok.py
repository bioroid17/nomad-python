from bs4 import BeautifulSoup
from requests import get


def extract_remoteok_jobs(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    response = get(url, headers={"User-Agent": "Kimchi"})
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # write your ✨magical✨ code here
        jobsboard = soup.find("table")
        jobs = jobsboard.find_all("tr", class_="job")
        results = []
        for job in jobs:
            _, info, tags, time, _ = job.find_all("td")
            # info
            a = info.find("a", class_="preventLink")
            title = a.find("h2").string.strip()
            company = info.find(
                "span", class_="companyLink").find("h3").string.strip()
            locations = []
            divs = info.find_all("div")
            for div in divs:
                locations.append(div.string.strip())
            locations.pop(-1)
            # tags
            anchors = tags.find_all("a")
            keywords = []
            for anchor in anchors:
                tag = anchor.find("div").find("h3").string.strip()
                keywords.append(tag)
            # time
            posted = time.find("time")
            posted_ago = posted.string
            if posted_ago is not None:
                posted_ago = posted_ago.strip()
            result = {
                "link": f"https://remoteok.com/remote-jobs{a['href']}",
                "company": company,
                "location": str(locations).replace(",", "|"),
                "position": title,
            }
            results.append(result)
        return results
    else:
        print("Can't get jobs.")
