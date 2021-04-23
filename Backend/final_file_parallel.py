import multiprocessing
from sentiment_analysis import get_tweets_main
from github_module import extract_repos
from youtube_module import extractYoutubeVideos
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
# creating a chrome instance.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--disable-gpu')
# redirecting to google.com
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--disable-gpu')
# # repalce the first argument with the path of your driver
driver = webdriver.Chrome(
    executable_path='C://Users//agarw//AppData//Local//Programs//Python//Python39//chromedriver.exe', options=chrome_options)


# function for getting links from the specified category
def link_from_category(category_link, category, n_pages):
    # class tag for categories
    class_from_categ = {"News": "dbsr", "Videos": "yuRUbf"}
    class_tag = ""
    class_tag = class_from_categ[category]

    results = []  # list for storing all the links

    for page in range(1, n_pages):
        url = category_link + str((page - 1) * 10)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search = soup.find_all('div', class_=class_tag)

        for h in search:
            results.append(h.a.get('href'))

    return results


def links_for_search(query, n_pages=10):
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
        category_link.append(
            driver.find_element_by_link_text(i).get_attribute('href'))

    # fetching all the links for news articles
    newslinks_results.append(link_from_category(
        category_link[0], "News", n_pages))

    return newslinks_results

def parallel_implementation(query):
    final_results = []

   # query = input("What do you want to search? ")
    start_time = time.time()
    with multiprocessing.Manager() as manager:
        processes = manager.list([manager.list() for i in range(4)])

        p1 = multiprocessing.Process(
            target=extractYoutubeVideos, args=(query, processes[0]))
        p2 = multiprocessing.Process(
            target=extract_repos, args=(query, processes[1]))
        p3 = multiprocessing.Process(
            target=get_tweets_main, args=(query, processes[2]))
        p4 = multiprocessing.Process(
            target=links_for_search, args=(query, processes[3]))

        p1.start()
        p2.start()
        p3.start()
        p4.start()

        p1.join()
        p2.join()
        p3.join()
        p4.join()

        # store the results in the global variable
        for i in processes:
            final_results.append(list(i))

    parallel_time = time.time() - start_time

    youTube_results, github_results, tweet_results, news_results = [], [], [], []

    youTube_results = final_results[0]


    github_results = final_results[1]


    tweet_results = final_results[2][0]


    news_results = final_results[3]


    return {'Youtube': youTube_results,
            'Github': github_results,
            'Tweets': tweet_results,
            'New': news_results,
            'Total Parallel': parallel_time}
