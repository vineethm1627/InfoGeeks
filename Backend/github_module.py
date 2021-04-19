from github import Github 
g = Github()
def extract_repos(userquery):
    tup=[]    
    repositories = g.search_repositories(query=userquery)
    for i in range(50):
        url='https://github.com/{}'.format(repositories[i].full_name)
        stars_count=repositories[i].stargazers_count
        tup.append([url, stars_count])
    return tup

def sortfun(Tuple):
    Tuple=sorted(Tuple, key=lambda x:x[1], reverse=True)
    return Tuple