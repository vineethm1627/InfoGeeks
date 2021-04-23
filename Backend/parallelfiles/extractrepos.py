# -*- coding: utf-8 -*-
"""extractrepos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OqLgs7huowi_g_75SlEKYfWs5mJsZnAZ
"""

'''
install the following in the main ipynb file

!pip install PyGithub

'''

from github import Github

def extract_repos(userquery, count=7):
    g = Github()
    repo_links = []
    repositories = g.search_repositories(query=userquery)
    for i in range(count):
        repo_links.append(tuple(['https://github.com/'+ repositories[i].full_name, repositories[i].stargazers_count]))
    return repo_links