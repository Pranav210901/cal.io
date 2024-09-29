from django.shortcuts import render
import requests
import json

def home(request):
    return render(request,'home.html')

def food_cal(request):
    if request.method == "POST":
        if 'query' in request.POST and 'serving_size' in request.POST:
            # Food Calorie Search
            query = request.POST.get('query', '')
            serving_size = int(request.POST.get('serving_size', 0))
            api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
            headers = {'X-Api-Key': 'YOUR-API-KEY'}

            try:
                api_request = requests.get(api_url + query, headers=headers)
                api_request.raise_for_status()  # Raise an HTTPError for bad responses
                data = api_request.json()
                items_list = data.get('items', [])

                if items_list:
                    item = items_list[0]  # Assume the first item is what we need
                    food = json.loads(json.dumps(item))  # Re-parse JSON to ensure it's correct
                else:
                    food = 'oops! There was an error'

            except requests.RequestException as e:
                food = f'Error: {str(e)}'

            return render(request, 'foodcal.html', {'food': food, 'serving_size': serving_size})

    # Handle GET request or other cases
    return render(request, 'foodcal.html', {'query': 'Enter a valid query or age/gender for BMR'})
