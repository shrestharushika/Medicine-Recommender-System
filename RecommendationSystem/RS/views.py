from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
import csv,io
import pandas as pd 
from django.contrib import messages
from RS.forms import UserForm,queryForm
from twilio.rest import Client
# Create your views here.

import sys

def home(request):
    return render(request,'home.html')

def new_user(request):
    form=UserForm()
    if request.method=='POST': 
        form=UserForm(request.POST)

        if form.is_valid():
             form.save()
             user=form.cleaned_data.get('Username')
            #  print(user)
            #  messages.success(request,"Registration is done for " + user)
             return redirect('/login')   
   
    return render(request,'new.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('Password')
        user1= authenticate(request,username=username,password=password)

        
        if user1 is not None:
            # print(user1)
            login(request,user1)
            return redirect('search/')
        else: 
            messages.info(request,"Username or Password is incorrect")   
    
    return render(request,'login.html',{})

def logout_request(request):
    sys.setrecursionlimit(1500)
    logout(request)

    return redirect('/login')  



def search_box(request):
    
    
    if request.method == "POST":
       
        s=request.POST['search']
        
        return redirect('/recommendation/'+s)

         
    return HttpResponse(render(request,'search_data.html'))  

#default rating=8

def recommendations(request,search):
    # print(search)
    
    html=""
    drugs_train = pd.read_csv("E:\Project Code\RecommendationSystem\RS\Drugs_train.csv")
    dataset=drugs_train.drop('drugName', axis=1).join(drugs_train['drugName'].str.split('/', expand=True).stack().reset_index(level=1, drop=True).rename('drugName'))
    medicines=[]
    
    
    
    
    y=[]
    x=[]
   
    # Append medicines that matches the search
    dic={}
    
    #match the search
    x=(dataset[dataset['condition']==search])

    # drop unnecessary columns
    data=['date','usefulCount']
    x=x.drop(data,axis=1)
    
   
    
    # droping duplicate values
    x1=x.drop_duplicates(subset = ["drugName"])
    
   
    # print(dataset)
    # print(len(x1))
    
    y=x1[x1['rating']>=9]
    medicines.append(y['drugName'].head(5))
    
    posts={
            "medicines":medicines,
            
            "search":search,
          }
    return HttpResponse(render(request,'recommendation.html',posts)) 

def view_details(request,medicine):
    data = pd.read_csv("E:\Project Code\RecommendationSystem\RS\Drugs_train.csv")
    dataset=data.drop('drugName', axis=1).join(data['drugName'].str.split('/', expand=True).stack().reset_index(level=1, drop=True).rename('drugName'))
    
    rev=[]
    sentiment=[]
    d=[]
   
   
    
    d=dataset[dataset['drugName']==medicine]
    rev= d['review']

   
    for i in rev:
        pred=[]
        pred=d[d['review']==i]['predicted']
        for p in pred:
            if p=="positive"   :
                sentiment.append((i,"Positive"))

            elif p=="Negative" :
                sentiment.append((i,"Negative")) 

            else:
                sentiment.append((i,"Neutral"))       
    
    
    positive=0
    neutral=0
    negative=0
     
    #Total no. of positive, neutral and negative reviews
    for i in rev:
        pred=[]
        
        pred=d[d['review']==i]['predicted']

        for p in pred: 
            if p=="positive":
                positive=positive+1
               
            elif p=="Negative":
                negative=negative+1
            else:
                neutral=neutral+1        
    
    # print(positive," ",len(sentiment))
    posts={"reviews":rev,
           "html":dataset,
           "sentiment":sentiment,
           "positive":positive,
           "negative":negative,
           "neutral":neutral }

    return HttpResponse(render(request,'details.html',posts))

def expert_advice(request):
        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)

        if request.method=="POST":
            query=request.POST['txt']
               
            
            message = client.messages.create(
                                        body=query,
                                        from_='',
                                        to=''
                                    )
                                    
            return redirect('/expert_advice')                    
        return HttpResponse(render(request,"doc.html",{}))    
