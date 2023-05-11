from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Run 3km a day"
    elif month == "february":
        challenge_text = "Don't eat as much"
    elif month == "march":
        challenge_text = "Practice guitar an hour per day"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
