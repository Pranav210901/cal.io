from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def bmr_cal(request):
    
    if request.method == "POST":
        
        # Retrieve form data
        age = int(request.POST['age'])
        gender = request.POST['gender']
        weight = float(request.POST['weight'])  # in kg
        height = float(request.POST['height'])  # in cm
        activity = request.POST.get('activity level', '')

        # Harris-Benedict equation to calculate BMR
        if gender == 'male':
            bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        else:
            bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        
        
        # Return the BMR to the template
        return render(request, 'bmrcal.html', {'bmr': bmr, 'activity':activity})


    # If it's a GET request, just return the page without BMR calculation
    return render(request, 'bmrcal.html')
