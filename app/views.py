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
import os

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'
    context["plans"] = readPlans()
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    
    context["plans"] = readPlans()
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

@login_required(login_url="/login/")
def update(request):
    context = {}
    context["plans"] = readPlans()
    if request.user.is_superuser:
        if request.method=="POST":
            plansDict= {
                "single": request.POST["singlePlan"],
                "batch": request.POST["batchPlan"]
            }
            monthly = request.POST["monthlyPlan"]
            monthly = list(monthly[1:-1].split(','))
            for month in monthly:
                print(month)
            monthly = [month.strip()[1:-1] for month in monthly]
            for month in monthly:
                print(month)
            plansDict["monthly"] = monthly;
            f= open("core/templates/plans.json", "w")
            json.dump(plansDict, f)
            f.close()
            context["plans"] = readPlans()
        return render(request, "adminPlanEdit.html", context)
    else:
        return render(request, "page-404.html")

def readPlans():
    f= open("core/templates/plans.json")
    return json.load(f)