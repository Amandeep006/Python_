import requests
import plotly.express as px

url="https://api.github.com/search/repositories"  
url+="?q=language:python+sort:stars+stars:>10000"

headers={"Accept": "application/vnd.github.v3+json"} 
r=requests.get(url, headers=headers) 
# print(f"Status code : {r. status_code}")

# Convert the response object to a dictionary
response_dict=r.json()
# print(f"Total repositories: {response_dict['total_count']}")
# print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repository information. With also adding custom Tool tips
repo_dicts= response_dict['items']
repo_names, stars, hover_texts,repo_links=[],[],[],[]
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])

    repo_url=repo_dict['html_url']
    repo_link=f"<a href='{repo_url}'> {repo_names} </a>"
    repo_links.append(repo_link)


    stars.append(repo_dict['stargazers_count'])
    # Build hover texts.
    owner=repo_dict['owner']['login']
    description=repo_dict['description']
    hover_text=f"{owner}<br />{description}"
    hover_texts.append(hover_text)


# Make visuliziation  with styling 

title="Most-Starred Python Projects on Github"
labels={'X':'repository','Y':'Stars'}
fig =px.bar(x=repo_links, y=stars, title=title, labels=labels,hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,yaxis_title_font_size=20)

# Customizing marker colors
fig.update_traces(marker_color='steelblue', marker_opacity=0.6)
fig.show()

"""
 A good place to start is with the article
“Plotly Express in Python,” at https://plotly.com/python/plotly-express. This is an
overview of all the plots you can make with Plotly Express, and you can find
links to longer articles about each individual chart type.
If you want to understand how to customize Plotly charts better, the
article “Styling Plotly Express Figures in Python” will expand on what you’ve
seen in Chapters 15–17. You can find this article at https://plotly.com/python/
styling-plotly-express.
For more about the GitHub API, refer to its documentation at https://
docs.github.com/en/rest. Here you’ll learn how to pull a wide variety of information from GitHub.
"""


