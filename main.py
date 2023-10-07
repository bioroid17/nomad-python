from requests import get

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com",

    "https://httpstat.us/101",
    "https://httpstat.us/200",
    "https://httpstat.us/300",
    "https://httpstat.us/404",
    "https://httpstat.us/502",
)

results = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code >= 500:
        results[website] = "Server error"
    elif response.status_code >= 400:
        results[website] = "Client error"
    elif response.status_code >= 300:
        results[website] = "Redirection"
    elif response.status_code >= 200:
        results[website] = "Successful"
    elif response.status_code >= 100:
        results[website] = "Informational"
    else:
        results[website] = "Unknown error"

print(results)
