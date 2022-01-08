from django.shortcuts import render
from datetime import datetime
from urllib.request import Request, urlopen
import json
import pandas as pd
import os

def stock_home(request):
    data = {}
    data['status'] = "not available"
    data['st_data'] = "nothing"
    # save the list of available files:================
    try:
        path = "stock_scrapper/saved_data/"
        data['files_list'] = os.listdir(path)
        data['files_list'] = [{'name':file,'symbol':file.split('_')[0], 'tf':file.split('_')[1], 'st_date':file.split('_')[2], 'end_date':file.split('_')[3][:-4]} for file in data['files_list']]
        #print("List of Files: ",data['files_list'])
    except Exception as e:
        print("Error getting saved files!")
    if request.method=='POST':
        d = {}
        d['symbol'] = request.POST['symbol']
        d['tf'] = request.POST['tf']
        d['st_date'] = request.POST['st_date']
        d['end_date'] = request.POST['end_date']
        d['st_date'] = d['st_date'][-2:]+"-"+d['st_date'][-5:-3]+"-"+d['st_date'][:4]
        d['end_date'] = d['end_date'][-2:]+"-"+d['end_date'][-5:-3]+"-"+d['end_date'][:4]
        d['st_date'] = get_t_stamp(d['st_date'])
        d['end_date'] = get_t_stamp(d['end_date'])
        d = get_data(d['symbol'],d['st_date'],d['end_date'],d['tf'])
        data['url'] = d['url']
        d = process_data(d['webpage'])
        data['st_data'] = d.to_dict('records')
        # Save some data for next page:==================
        data['status'] = "available"
        data['symbol'] = request.POST['symbol']
        data['tf'] = request.POST['tf']
        data['st_date'] = request.POST['st_date']
        data['end_date'] = request.POST['end_date']
        if(request.POST['submit_button'] == ' Get Data '):
            pass
        else:
            name = data['symbol']+"_"+data['tf']+"_"+data['st_date']+"_"+data['end_date']+".csv"
            d.to_csv("stock_scrapper/saved_data/"+name,index=False)
    else:
        pass
    return render(request,'stocks_home.html',data)

def get_data(symbol,st,et,r):
    if(st!=1 and et!=1 and (r=="1D" or r=="1")):
        url="https://priceapi.moneycontrol.com/techCharts/techChartController/history?symbol="
        url=url+symbol+"&resolution="+r+"&from="+str(st)+"&to="+str(et)
        return bring_data(url)
    else:
        print("No Data Found!!")
        return 1
    
def get_t_stamp(date):
    try:
        return int(datetime.timestamp(datetime.strptime(date,'%d-%m-%Y')))
    except Exception as e:
        print("get_t_stamp: Exception occured :-",str(e))
        return 1

def bring_data(url):
    try:
        d = {}
        d['url'] = url
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        client = urlopen(req)
        webpage = client.read()
        client.close()
        d['webpage'] = webpage
        return d
    except Exception as e:
        print("bring_data: Exception occurred:-",str(e))
        return 1

def process_data(page):
    try:
        data = json.loads(page)
        d = pd.DataFrame()
        d["date"] = [datetime.fromtimestamp(int(t)).date() for t in data['t']]
        d["time"] = [datetime.fromtimestamp(int(t)).time() for t in data['t']]
        d["open"] = data['o']
        d["close"] = data['c']
        d["high"] = data['h']
        d["low"] = data['l']
        d["volume"] = data['v']
        return d
    except Exception as e:
        print("process_data: Exception Occured:- ",str(e))
        return 1