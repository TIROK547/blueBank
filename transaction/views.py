from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

BOODJE = 100000
def my_account(request,username):
    return render(request,"./templates/transaction/main.html")

def get_loan(request,darkhast):
    global BOODJE
    if BOODJE < darkhast:
        return HttpResponse("successful")
    else:
        return HttpResponse("ERROR")