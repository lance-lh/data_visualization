import requests

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
for repo_dict in repo_dicts:
    print("Name:",repo_dict['name'])
    print("Owner:",repo_dict['owner']['login'])
    print("Stars:",repo_dict['stargazers_count'])
    print("Repository:",repo_dict['html_url'])
    print("Created:",repo_dict['created_at'])
    print("Updated:",repo_dict['updated_at'])
    print("Description:",repo_dict['description'])