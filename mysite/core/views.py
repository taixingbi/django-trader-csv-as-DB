import os
import json

import logging
logger = logging.getLogger(__name__)
from django.http import HttpResponse

from django.http import Http404
from django.http import HttpResponseServerError
from django.core.exceptions import EmptyResultSet

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.http import JsonResponse
from django.utils import timezone


# from django.contrib.staticfiles import finders
import pandas as pd 

from django.template.response import TemplateResponse


from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import logout

import time

from django.conf import settings

# from database.models import Teleconference_transcribe
# from database.serializers import Teleconference_transcribeSerializer

from django.conf import settings

# from django.conf.urls import url

from datetime import datetime
import time

import logging

from stock.module import *
from stock.strategy import *
from stock.csvSell import *

from stock.csvSellLog import *
cSVSellLog = CSVSellLog()

# Get an instance of a logger
logger = logging.getLogger(__name__)


nowtime = str(datetime.now()).split(".")[0]


# views
class Home(TemplateView):
    template_name = 'home.html'


cSVSell = CSVSell()

def update_view(request):
    logout(request)

    if request.method == 'POST':
        clean = request.POST.get('clean')
        # reset = request.POST.get('reset')

        if clean:
            print("csv was cleaned")
            cSVSell.clean()
        else:
            print("add stock")
            stock = request.POST.get('stock')
            stopPercentage = request.POST.get('stopPercentage')
            stocks= stock.split()
            stopPercentages= stopPercentage.split()
            print(stocks,stopPercentages)
            cSVSell.clean()
            for i , stock in enumerate(stocks):
                cSVSell.add(stocks[i], stopPercentages[i])

    args = {}
    args['isRefresh'] = False
    return render(request,'update.html')

def sell_view(request, template_name="sell.html"):
    args = {}

    price = " "
    df = cSVSell.read()
    names = df['name'].to_list()
    for name in names:
        price +=  name + " $" + str(CheckPrice(name).live())  + " "

    args['price'] = getTimeNow() + " " +  price
    args['isRefresh'] = True
    args['log'] = cSVSellLog.read()
    return TemplateResponse(request, template_name, args)

# -----------------------------------------for api-------------------------------------
class Demo(): 

    #/version/
    def version(request):  
        print("\n\n*************************************version*************************************")
        logger.info('version info!')
        dataJson= {
            "version": "1.0"
        }

        return JsonResponse(dataJson)

    #/test/s3/
    def s3(request):  
        print("\n\n************************************* s3 test*************************************")

        #bucket='thrivee-dev/audiotranscribe'
        bucket=  'thrivee-dev'

        key= 'audiotranscribe/test.wav'

        fileName= 'media/' + key.split('/')[1]
        print(fileName)
        res= s3Bucket(bucket, key, fileName).loadFile()

        data= {
            "s3": res,
        }
        
        return JsonResponse(data)
    
    #/test/db
    def db(request):  
        print("\n\n************************************* db test*************************************")
        
        # DBRead().peak("QQQ")
        # DBRead().updatePeak("QQQ", 555)
        # DBRead().updateOrder_pending()

        # DBRead().valley("QQQ")
        # DBRead().updateValley("QQQ", 1000)

        order.order('BYFC', 1, 'sell', 1.2, 0.7)
        # order.buy('AMD', 1, 'buy', 110)

        data= {
            "db test": "data"
        }
        
        return JsonResponse(data)

    def ses(request):  
        print("\n\n************************************* ese test*************************************")

        SES().gmail()

        data= {
            "ses": "ses",
        }
        
        return JsonResponse(data)

    #/api/ticker/<key>
    def ticker(request, key):  #s3 key
        print("\n\n************************************* ticker *************************************")
        print(key)
        # robinhood(key) #symbol
        
        data= {
            "ticker": key,
        }
        
        return JsonResponse(data)


    #/api/demo
    def demo(request):  #s3 key
        print("\n\n************************************* demo *************************************")

        data= {
            "demo": "demo",
        }       

        if request.method == 'POST':
            print("POST...")
            
            form = NameForm(request.POST)
            # # check whether it's valid:
            # if form.is_valid():
            #     data= {
            #         "stock": form,
            #     } 
            #     return JsonResponse(data)

            data= {
                "stock": form,
            } 

            return "form"

        if request.method == 'GET':
            print("GET...")

        return JsonResponse(data)

        # df= pd.DataFrame(data, index=[0])
        # return HttpResponse( df.to_html() )
    

          
