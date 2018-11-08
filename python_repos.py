import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# call Github API and store response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code) # status code 200 indicates request successful

# store API response in a variable
response_dict = r.json()    # convert info into python dict

# deal with results
# print(response_dict.keys())
print("Total respositories:",response_dict['total_count'])

# explore more info about repositories
repo_dicts = response_dict['items'] # items is a list but contain many dicts
print("Repositories returned:",len(repo_dicts)) # how many repos

# # explore the first repo
# repo_dict = repo_dicts[0]
# print("\nKeys:",len(repo_dict)) # how many keys
# for key in sorted(repo_dict.keys()):
#     print(key)
#
# print("\nSelected information about first repository:")
# print("Name:",repo_dict['name'])
# print("Owner:",repo_dict['owner']['login'])
# print("Stars:",repo_dict['stargazers_count'])
# print("Repository:",repo_dict['html_url'])
# print("Created:",repo_dict['created_at'])
# print("Updated:",repo_dict['updated_at'])
# print("Description:",repo_dict['description'])


print("\nSelected information about each repository:")
names, stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# visualize
my_style = LS('#333366',base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('',stars)
chart.render_to_file('python_repos.svg')
