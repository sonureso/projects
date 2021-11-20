from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from datetime import datetime
from urllib.request import Request, urlopen
import json
import pandas as pd

def detect_home(request):
    return render(request,'face_detect.html')

def detect_face(request):
    data = {}
    data['d'] = "Nothing"
    print("step-01")
    if request.method=='POST':
        print("step-02")
        what = request.POST['what'] 
        if(what=='detect_face'): 
            print("step-03")
            face_img= request.files['face_img'] 
            print("Face: ",face_img) 
        return HttpResponse(data)
    else:
        return HttpResponse(data)


