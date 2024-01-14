from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from datetime import datetime
from urllib.request import Request, urlopen
import json
import pandas as pd
from face_detector.models import tempItems
import cv2
import imutils # required by resize function

def detect_home(request):
    return render(request,'face_detect.html')

def detect_face(request):
    data = {}
    print("Detect Face Called.")
    data['status']=False
    if request.method=='POST':
        what = request.POST['what'] 
        if(what=='save_face'):
            face_img = request.FILES.get('face_img',False)
            try:
				# case: when there is image already saved.
                obj = tempItems.objects.get(name="img_01")
                obj.img.delete(False)
                obj.img = face_img
                obj.img.name = "img_01.jpg"
                obj.save()
                data['status'] = True
                data['img'] = obj.img.name
                print("Image: ",data['img'])
                #print("Try BLock completed.")
            except:
                new = tempItems(img=face_img,name="img_01")
                new.img.name = "img_01.jpg"
                new.save()
                data['status'] = True
                data['img'] = new.img.name
                print("Image: ",data['img'])
                #print("Except BLock completed.")
            #print("Face: ",face_img)
        elif(what=='detect_face'):
            try:
                before = datetime.now()
                face_cascade = cv2.CascadeClassifier('static/cascades/haarcascade_frontalface_default.xml')
                img = cv2.imread('static/temp/img_01.jpg')
                #height, width = img.shape[:2]
                img = imutils.resize(img, width=900)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 11)
                # faces = face_cascade.detectMultiScale(gray, 1.05, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 6)
                cv2.imwrite("static/temp/img_01_detected.jpg", img)
                data['status'] = True
                data['face_count'] = len(faces)
                data['time_taken'] = str(datetime.now() - before)
                print("Time: ",data['time_taken'])
            except Exception as e:
                print("Exception Occurred here: ",e)
                
        return JsonResponse(data)
    else:
        return render(request,'face_detect.html',data)


