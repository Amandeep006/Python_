import requests 

"""Processing an API Response"""
"""
 # Make an API call and check the response.

# We braeak the url into two line. 1. it is the main part of the url and 2. It query string.  We have included one more condition to the original query
# string: stars:>10000, which tells GitHub to only look for Python repositories
# that have more than 10,000 stars
url="https://api.github.com/search/repositories"  
url+="?q=language:python+sort:stars+stars:>10000"

headers={"Accept": "application/vnd.github.v3+json"} 
r=requests.get(url, headers=headers) 
print(f"Status code : {r. status_code}")
# We asked the API to return the information in JSON format, so we use the json() method to convert the information to a Python dictionary 

# Convert the responses object to dictionary.
response_dict=r.json() # the response object has an attributes called an status_code. and  
print(response_dict.keys())
"""



"""Working with the Response Dictionary"""

url="https://api.github.com/search/repositories"  
url+="?q=language:python+sort:stars+stars:>10000"

headers={"Accept": "application/vnd.github.v3+json"} 
r=requests.get(url, headers=headers) 
print(f"Status code : {r. status_code}")

# Convert the response object to a dictionary
response_dict=r.json()
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts= response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
# repo_dict=repo_dicts[0]
# print("\nSelected information about the first repository:")
# print(f"Name: {repo_dict['name']}")
# print(f"Owner: {repo_dict['owner']['login']}")
# print(f"Stars: {repo_dict['stargazers_count']}")
# print(f"Repository: {repo_dict['html_url']}")
# print(f"Created: {repo_dict['created_at']}")
# print(f"Updated: {repo_dict['updated_at']}")
# print(f"Description: {repo_dict['description']}")

# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)


"""Summarization of the Top repository."""
print("\nSelected information about each repository: ")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")