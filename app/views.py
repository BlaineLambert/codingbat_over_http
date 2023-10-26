from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.

def near_hundred(request: HttpRequest, num) -> HttpResponse:
    if abs(num - 100) <= 10 or abs(num - 200) <= 10:
        return HttpResponse(True)
    else:
        return HttpResponse(False)
    
def string(request: HttpRequest, char) -> HttpResponse:
    result = ""
    for i in range(len(char)):
        result += char[:i + 1]

    return HttpResponse(result)

def counter(request: HttpRequest, list) -> HttpResponse:
    cat_count = list.count("cat")
    dog_count = list.count("dog")

    return HttpResponse(cat_count == dog_count)

def numcount(request: HttpRequest, num1, num2, num3) -> HttpResponse:
    if num1 == num2 and num1 == num3 and num2 == num3:
        return HttpResponse(0)
    if num1 == num2 and num1 != num3 or num1 == num2 and num2 != num3:
        return HttpResponse(num3)
    if num1 == num3 and num1 != num2 or num1 == num2 and num3 != num2:
        return HttpResponse(num2)
    if num1 != num2 and num1 != num3 and num2 != num3:
        return HttpResponse(num1 + num2 + num3)