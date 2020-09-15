import requests

class Repository():

    def __init__(self, item):
        self._item = item
        print(self._item)


user_input = input(f'Enter your gtihub username \n')

response = requests.get(f'https://api.github.com/users/{user_input}/repos')

# print(response.json()[2]["name"])
# print(len(response.json()))

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')


names = [li['name'] for li in response.json()]
# print(names)

for item in enumerate(names, 1):
    #print(item)
    item = Repository(f'{item}')

user_input_2 = input(f"Enter the id of the repo you're interested in\n")


print('id:' + str(response.json()[int(int(f'{user_input_2}')-1)]['id']))
print('name:' + str(response.json()[int(int(f'{user_input_2}')-1)]['name']))
print('no of forks:' + str(response.json()[int(int(f'{user_input_2}')-1)]['forks_count']))
print('created:' + str(response.json()[int(int(f'{user_input_2}')-1)]['created_at']))
print('language:' + str(response.json()[int(int(f'{user_input_2}')-1)]['language']))
print('link to repo: ' + str(response.json()[int(int(f'{user_input_2}')-1)]['html_url']))





