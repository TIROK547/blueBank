from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

BOODJE = 100000

def my_account(request, username):
    return render(request, "transaction/main.html", context={'username': username})

def get_loan(request,darkhast):
    global BOODJE
    if BOODJE > darkhast:
        BOODJE -= darkhast
        return HttpResponse(f"successful remaining boodje: {BOODJE}")
    else:
        return HttpResponse("ERROR")