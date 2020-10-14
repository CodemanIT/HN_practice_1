from django.shortcuts import render
from django.http import HttpResponse
from .methods import reverseString

def index(request):
    if request.method == "POST":
        data = request.POST.get("index")
        return render(request,'reverse/output.html',{'output':reverseString(data)})
    return render(request,'reverse/mainPage.html')



