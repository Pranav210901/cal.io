import requests
import json

query = '1lb brisket'
api_url = 'https://api.calorieninjas.com/v1/nutrition?query={}'.format(query)
response = requests.get(api_url, headers={'X-Api-Key': 'nEW83hqBTmgNZry0Y7UfOQ==mmKNGbDyQnao1OZg'})
# if response.status_code == requests.codes.ok:
#     print(response.json())
# else:
#     print("Error:", response.status_code, response.text)

if response.status_code == requests.codes.ok:
    try:
        # Parse the JSON response
        data = response.json()

        # Access the 'items' list
        items_list = data.get('items', [])

        # Loop through items and print each one
        for i in items_list:
            item = i
        item_string = json.dumps(item, indent = 4)

    except ValueError:  # In case the response is not JSON
        print("Failed to decode JSON response:", response.text)
else:
    print(f"Error {response.status_code}: {response.text}")
print(type(item_string))
print(type(item))
x = json.loads(item_string)
print(x)
# if response.status_code == requests.codes.ok:
#     print(response.json())
# else:
#     print("Error:", response.status_code, response.text)
# print(type(response))
# print("#####################################")

# query = '1lb brisket and fries'
# api_url1 = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
# response1 = requests.get(api_url1, headers={'X-Api-Key': 'nEW83hqBTmgNZry0Y7UfOQ==1zTeBTnlNFGPqkJv'})
# if response1.status_code == requests.codes.ok:
#     print(response1.json())
# else:
#     print("Error:", response1.status_code, response1.text)

# print(type(response1))



