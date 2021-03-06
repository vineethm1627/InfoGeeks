from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

chrome_options= webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--use-gl=swiftshader")
chrome_options.add_argument("--ignore-gpu-blacklist")
chrome_options.add_argument("--disable-webgl")
#chrome_options.add_argument('--enable-webgl')
driver = webdriver.Chrome(executable_path="C://Users//agarw//AppData//Local//Programs//Python//Python39//chromedriver.exe", options=chrome_options) #place the path of chromedriver.exe from your pc in executable_path


# function for getting links from the specified category
def link_from_category(category_link, category, n_pages):
    class_from_categ = {"News": "dbsr", "Videos": "yuRUbf"}  # class tag for categories
    class_tag = ""
    class_tag = class_from_categ[category]

    results = []  # list for storing all the links

    for page in range(1, n_pages):
        url = category_link + str((page - 1) * 10)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        search = soup.find_all("div", class_=class_tag)

        for h in search:
            results.append(h.a.get("href"))

    return results


def links_for_search(query, n_pages=6):
    newslinks_results = []

    driver.get("https://www.google.com")

    # accessing the search bar and searching the specified query
    search_bar = driver.find_element_by_name("q")
    search_bar.clear()
    search_bar.send_keys(query)
    search_bar.send_keys(Keys.RETURN)

    # fetching the news and videos links for the specified query
    category_list = ["News"]
    category_link = []
    for i in category_list:
        category_link.append(driver.find_element_by_link_text(i).get_attribute("href"))

    # fetching all the links for news articles
    newslinks_results.append(link_from_category(category_link[0], "News", n_pages))
    return newslinks_results
