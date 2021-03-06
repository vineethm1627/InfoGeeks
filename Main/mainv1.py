# -*- coding: utf-8 -*-
"""mainV1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/194nqQC13vaOcAf7WEJrXTYClChn5yNDa
"""

#set up for selenium

!pip install selenium
!apt-get update # to update ubuntu to correctly run apt install
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

# setup with tweets
!pip install tweepy
!pip install textblob

!pip install PyGithub

!pip install pymp-pypi

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# redirecting to google.com 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
 # If you are using it in your local system, repalce the first argument with the path of your chromium.exe file.
 # The driver should be into the directory where python is installed. Add the driver's path in  the system variables path also.
 

# function for getting links from the specified category
def link_from_category(category_link, category, n_pages):
  class_from_categ = {"News":"dbsr", "Videos":"yuRUbf"} #class tag for categories
  class_tag = ""
  class_tag = class_from_categ[category]

  results = [] # list for storing all the links


  for page in range(1, n_pages):
    url = category_link +  str((page - 1) * 10) 
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    search = soup.find_all('div', class_=class_tag )

    for h in search:
        results.append(h.a.get('href'))

    
  return results

def links_for_search(query, newslinks_results, n_pages=10):
  newslinks_results = list(newslinks_results)

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
    category_link.append(driver.find_element_by_link_text(i).get_attribute('href'))


  # fetching all the links for news articles
  newslinks_results.append(link_from_category(category_link[0], "News",n_pages))

from extract_Videos import extractYoutubeVideos
from extractrepos import extract_repos
from sentiment_analysis_twitter import get_tweets_main

start_time = time.time()

videos_links = []
extractYoutubeVideos("deep learning",videos_links)

repo_links = []
extract_repos("deep learning", repo_links)

tweets = []
get_tweets_main = get_tweets_main("deep learning", tweets)

news_links = []
links_for_search("deep learning", news_links)

print("Time for serial implementation:",time.time()-start_time)

from multiprocessing import Process

query = input("What do you want to search? ")


start_time = time.time()

results = [ [] for i in range(4) ]

p1 = multiprocessing.Process(target=extractYoutubeVideos, args=(query, results[0]))
p2 = multiprocessing.Process(target=extract_repos, args=(query, results[1]))
p3 = multiprocessing.Process(target=get_tweets_main, args=(query, results[2]))
p4 = multiprocessing.Process(target=links_for_search, args=(query, results[3]))

p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

print("Time for parallel implementation:",time.time()-start_time)