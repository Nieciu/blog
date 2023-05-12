from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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


def index(request):
    list_items =""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge",args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):

    if month > 12:
        return HttpResponseNotFound("This month is not supported!")

    months = list(monthly_challenges.keys())
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html")
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
