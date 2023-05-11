from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Run 3km a day",
    "february": "Don't eat as much",
    "march": "Practice guitar an hour per day",
    "april": "Practice guitar an hour per day",
    "may": "Practice guitar an hour per day",
    "june": "Practice guitar an hour per day",
    "july": "Practice guitar an hour per day",
    "august": "Practice guitar an hour per day",
    "september": "Practice guitar an hour per day",
    "october": "Practice guitar an hour per day",
    "november": "Practice guitar an hour per day",
    "december": "Practice guitar an hour per day"
}


def monthly_challenge_by_number(request, month):

    if month > 12:
        return HttpResponseNotFound("This month is not supported!")

    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/"+redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
