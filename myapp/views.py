from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, "home.html")

def result (request):
    num = int(request.GET['num'])
    if num == 4 :
        result = "4팀 짱"
    else:
        result = "화이팅"
    return render (request, "result.html", {'result':result})
    