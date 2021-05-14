# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
import json
from .models import History
from authentication.models import Profile
from django.contrib.auth.models import User

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'
    context["plans"] = readPlans()
    context["history"] = History.objects.filter(user=request.user)
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    context["plans"] = readPlans()
    context["history"] = History.objects.filter(user=request.user)

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login")
def updateProfile(request):
    context = {}
    context["plans"] = readPlans()
    context['segment'] = 'index'
    context["history"] = History.objects.filter(user=request.user)
    if request.method == "POST":
        user = request.user
        if not Profile.objects.filter(user=user).exists():
                userProfile= Profile(user = user)
                userProfile.save()
        userProfile = Profile.objects.get(user=user)
        userProfile.address = request.POST["address"]
        userProfile.city = request.POST["city"]
        userProfile.state = request.POST["state"]
        userProfile.zip_code = request.POST["zcode"]
        userProfile.phone = request.POST["pNo"]
        userProfile.save()
        user.first_name = request.POST["fname"]
        user.last_name = request.POST["lname"]
        user.email = request.POST["mail"]
        user.save()
    return render(request, "editProfile.html", context)

@login_required(login_url="/login/")
def update(request):
    context = {}
    context["plans"] = readPlans()
    if request.user.is_superuser:
        if request.method=="POST":
            plansDict= {
                "single": float(request.POST["singlePlan"]),
                "batch": float(request.POST["batchPlan"])
            }
            monthly = request.POST["monthlyPlan"]

            monthly = list(monthly[1:-1].split(','))
            monthly = [month.strip(' []') for month in monthly]
            monthlyF = []
            for i in range(0, len(monthly), 2):
                print(monthly[i], monthly[i+1])
                monthlyF.append([float(monthly[i]),int(monthly[i+1])])
            print(monthlyF)
            plansDict["monthly"] = monthlyF;
            monthlyP = [];
            for (x,y) in monthlyF:
                monthlyP.append("$"+str(x)+" for "+str(y)+" searches.")
            print(monthlyP)
            plansDict["monthlyPretty"] = monthlyP;
            f= open("core/config/plans.json", "w")
            json.dump(plansDict, f)
            f.close()
            context["plans"] = readPlans()
        return render(request, "adminPlanEdit.html", context)
    else:
        return render(request, "page-404.html")

def readPlans():
    f= open("core/config/plans.json")
    return json.load(f)