from __future__ import unicode_literals
import datetime
import random
from django.shortcuts import render, redirect

def reset(request):
    request.session['gold_score'] = 0
    request.session['activity'] = []
    return render(request, 'index.html')

def index(request):
    if "gold_score" not in request.session:
        request.session["gold_score"] = 0

    if "activity" not in request.session:
        request.session["activity"] = []
        
    gold_score = request.session["gold_score"]
    context = {
        "gold_score": gold_score,
        "activity": request.session["activity"]
    }
    print("def index")
    return render(request, 'index.html', context)

def processMoney(request):
    print("def processMoney")
    if request.method == "POST":
        if request.POST['action'] == "farm":
            print("Adding gold in farm")
            gold = random.randint(10, 20)
            request.session['gold_score'] += gold
            text= f'you entered a form earned {gold} gold'+'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            request.session['activity'].append(text)

        elif request.POST['action'] == "cave":
            gold = random.randint(10, 20)
            request.session['gold_score'] += gold
            text= f'you entered a form earned {gold} gold'+'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            request.session['activity'].append(text)

        elif request.POST['action'] == "house":
            gold = random.randint(10, 20)
            request.session['gold_score'] += gold
            text= f'you entered a form earned {gold} gold'+'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            request.session['activity'].append(text)

        elif request.POST['action'] == "quest":
            gold = random.randrange(-50, 50)
            request.session['gold_score'] += gold
            if(gold<0):
                text = f'you faild a form and lost {gold}. Once'+'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
                request.session['activity'].append(text)
            else:
                text= f'you entered a form earned {gold} gold'+'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
                request.session['activity'].append(text)
    return redirect('/')

