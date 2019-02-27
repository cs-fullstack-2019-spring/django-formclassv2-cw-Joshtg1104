from django.shortcuts import render
from django.http import HttpResponse
from .forms import employeeApply


# Create your views here.

# function that renders the employeeApply form on the home.html and
# the submitted information onto the employAppResylts.html
def index(request):
    if (request.method == 'POST'):
        print(request.POST)
        context = {
            "name": request.POST["name"],
            "dateOfBirth": request.POST["date_of_birth"],
            "position": request.POST["position_applying_to"],
            "salary": request.POST["desired_salary"]
        }
        return render(request, "EmployApp/employAppResults.html", context)
    else:
        emApp = employeeApply()
        context = {
            "emApp": emApp
        }

        return render(request, "EmployApp/home.html", context)
