from django.shortcuts import render

# Create your views here.
def home(req):
    context = {}
    context['text1'] = "TEXT 1"
    context['number1'] = 123456
    context['list1'] = [1,2,3,4,5,6]

    return render(req, "index.html", context)