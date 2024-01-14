# ************************************************ #
#      views.py for stock_scrapper app
# ************************************************ #
from django.shortcuts import render
from datetime import datetime
from urllib.request import Request, urlopen
import json
import pandas as pd
import os

# URL: localhost/stock_scrapper/
def stock_home(request):
    data = {}
    data['status'] = "not available"
    data['st_data'] = "nothing"
    # save the list of available files: ================
    try:
        path = "stock_scrapper/saved_data/"
        data['files_list'] = os.listdir(path)
        data['files_list'] = [{'name':file,'symbol':file.split('_')[0], 'tf':file.split('_')[1].split('.')[0]} for file in data['files_list']]
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
            sync_dataset(data, d)
    else:
        pass
    return render(request,'stocks_home.html',data)

def sync_dataset(data, new_df):
    path = "stock_scrapper/saved_data/"+data['symbol']+"_"+data['tf']+".csv"
    name = data['symbol']+"_"+data['tf']+".csv"
    if(os.path.exists(path)):
        old_df = pd.read_csv(path)
        old_df = old_df.astype('str')
        new_df = new_df.astype('str')
        final_df = pd.concat([old_df,new_df]).drop_duplicates().sort_values(by='timestamp', ascending=False).astype('str')
        final_df.to_csv(path, index = False)
        print("Old file: ",name,"has row count: ", old_df.shape[0])
        print("New file: ",name,"has row count: ", new_df.shape[0])
        print("Merged file: ",name,"has row count: ", final_df.shape[0])
    else:
        print("Creating Data file: ",data['symbol']+"_"+data['tf']+".csv", end = " ")
        new_df.to_csv(path, index = False)
        print(new_df.shape[0],"Rows -> Completed!")

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
        print("01. Check your network connection!")
        print("02. ERROR in bring_data: Exception occurred:-",str(e))
        return 1

def process_data(page):
    try:
        data = json.loads(page)
        d = pd.DataFrame()
        d["timestamp"] = data['t']
        # d["date"] = [datetime.fromtimestamp(int(t)).date() for t in data['t']]
        d["day"] = [datetime.fromtimestamp(int(t)).date().day for t in data['t']]
        d["month"] = [datetime.fromtimestamp(int(t)).date().month for t in data['t']]
        d["year"] = [datetime.fromtimestamp(int(t)).date().year for t in data['t']]
        d["time"] = [str(datetime.fromtimestamp(int(t)).time()) for t in data['t']]
        d["open"] = data['o']
        d["close"] = data['c']
        d["high"] = data['h']
        d["low"] = data['l']
        d["volume"] = data['v']
        return d
    except Exception as e:
        print("process_data: Exception Occured:- ",str(e))
        return 1