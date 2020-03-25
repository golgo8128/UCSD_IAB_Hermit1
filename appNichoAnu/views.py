from django.shortcuts import render

# Create your views here.

import os
from datetime import datetime, timedelta
import dateutil.parser

import getpass

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

from django.conf import settings
from django.template import RequestContext, loader
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect #, JsonResponse
from django.urls import reverse

from ipware.ip import get_ip

from .models import *
from .modules.to_networkx1_6 import to_networkx

from UCSD_IAB_Usefuls.Time.timezone1 import get_tzone

from FileDirPath.mkdir_on_absent import mkdir_on_absent
from FileDirPath.File_Path1 import rs_filepath_info

from Usefuls.TimeStamp_HashFile1_1 import TimeStamp_HashFile

client_ip_log_file = os.path.join(settings.UCSD_IAB_WORKDIR,
                                  "Media", "appNichoAnu", "Log",
                                  "client_ip_log1.pkl")

def index(request):

    timezone.activate(get_tzone(request.user))  

    ipaddr = get_ip(request)
    if ipaddr:        
        mkdir_on_absent(rs_filepath_info(client_ip_log_file)[ "foldername" ])
        ip_log = TimeStamp_HashFile(client_ip_log_file)
        ip_log.stamp(ipaddr)

    contxt = RequestContext(request, { "NichoNode" : NichoNode,
                                       "NichoEdge" : NichoEdge,
                                       "settings"  : settings,
                                       "apache_user" : getpass.getuser(),
        "acount_minus_wk3": len(ip_log.get_keys_timerange(timedelta(days = 21), timedelta(days = 14))),
        "acount_minus_wk2": len(ip_log.get_keys_timerange(timedelta(days = 14), timedelta(days =  7))),
        "acount_minus_wk1": len(ip_log.get_keys_timerange(timedelta(days =  7), timedelta(days =  0))),
         }) # {{ message|safe }}
    templt = loader.get_template("appNichoAnu/map_Anurag1_3.html")
    
    return HttpResponse(templt.render(contxt)) 


def pub_db_tools(request):

    contxt = RequestContext(request, { })
    templt = loader.get_template("appNichoAnu/pub_db_tools1.html")
    
    return HttpResponse(templt.render(contxt))     

def survey(request):

    contxt = RequestContext(request, { })
    templt = loader.get_template("appNichoAnu/survey1.html")
    
    return HttpResponse(templt.render(contxt))    

def member(request):

    contxt = RequestContext(request, { })
    templt = loader.get_template("appNichoAnu/nichoanu_member1.html")
    
    return HttpResponse(templt.render(contxt))     
    
def material_src(request):
    
    contxt = RequestContext(request, { })
    templt = loader.get_template("appNichoAnu/material_src1.html")
    
    return HttpResponse(templt.render(contxt))    
    
def history(request):

    contxt = RequestContext(request, { })
    templt = loader.get_template("appNichoAnu/history_Anurag1.html")
    
    return HttpResponse(templt.render(contxt))  

def work_record(request):

    contxt = RequestContext(request, { })
    templt = loader.get_template("appNichoAnu/work_record_Golgo1.html")
    
    return HttpResponse(templt.render(contxt)) 

def blog(request):

    contxt = RequestContext(request, { })
    templt = loader.get_template("appNichoAnu/blog1.html")
    
    return HttpResponse(templt.render(contxt))   
