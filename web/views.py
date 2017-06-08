# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import User, Expense, Income, Token


@csrf_exempt
def submit_expense(request):
    """ User submits an expense. """

    print "I am in submit expense."

    # TODO: Validate date; Token might be fake. User might be fake. Text might be fake. Amount might be fake.
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    this_text = request.POST['text']
    this_amount = request.POST['amount']
    if 'date' not in request.POST:
        this_date = timezone.now()
    else:
        this_date = request.POST['date']

    Expense.objects.create(user=this_user, text=this_text, amount=this_amount, date=this_date)

    return JsonResponse({
        'status': 'ok',
    })


@csrf_exempt
def submit_income(request):
    """ User submits an income. """

    print "I am in submit income."

    # TODO: Validate date; Token might be fake. User might be fake. Text might be fake. Amount might be fake.
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    this_text = request.POST['text']
    this_amount = request.POST['amount']
    if 'date' not in request.POST:
        this_date = timezone.now()
    else:
        this_date = request.POST['date']

    Income.objects.create(user=this_user, text=this_text, amount=this_amount, date=this_date)

    return JsonResponse({
        'status': 'ok',
    })
