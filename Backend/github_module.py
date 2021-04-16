from github import Github 

g = Github()

#userquery=input('Enter your search query-')

#sort_flag=input('Do you want to sort the results based on the number of stars on the repositories? (y/n)-')
def extract_repos(userquery):
    tup=[]    
    repositories = g.search_repositories(query=userquery)
    for i in range(50):
        url='https://github.com/{}'.format(repositories[i].full_name)
        #print(url)
        stars_count=repositories[i].stargazers_count
       # print('Number of Stars on the repo=', stars_count)
        tup.append([url, stars_count])
    return tup
        

def sortfun(Tuple):
    Tuple=sorted(Tuple, key=lambda x:x[1], reverse=True)
    return Tuple

# def apply_sort(flag, Tuple):
#     if(flag=='y'):
#         new_tup=sortfun(Tuple)
#     for i in  new_tup:
#         print(i)
    
#extract_repos(userquery)

#apply_sort(sort_flag, tup)