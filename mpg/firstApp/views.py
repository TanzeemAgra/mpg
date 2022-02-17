from django.shortcuts import render
import joblib
import pandas as pd
import sklearn

# Create your views here.

def mpg(request):
    return render(request, 'mpg.html')

def result2(request):
    
    #clm = joblib.load('RFModelforMPG1.pkl')
    modelReload=joblib.load('RFModelforMPG.pkl')
    """lis = []
    
    lis.append()
    lis.append(request.GET['displacement'])
    lis.append(request.GET['horsepower'])
    lis.append(request.GET['weight'])
    lis.append(request.GET['acceleration'])
    lis.append(request.GET['model_year'])
    lis.append(request.GET['origin'])"""
    
    a=request.GET['cylinders']
    
    
    temp= {}
    temp['cylinders'] = a
    temp['displacement'] = request.GET['displacement']
    temp['horsepower']=request.GET['horsepower']
    temp['weight']=request.GET['weight']
    temp['acceleration']=request.GET['acceleration']
    temp['model_year']=request.GET['model_year']
    temp['origin']=request.GET['origin']
    
    testDtaa=pd.DataFrame({'x':temp}).transpose()
    
    answer1= modelReload.predict(testDtaa)[0]
    
    
    #answer1 = clm.predict([lis])
    return render(request, "mpg.html", {'answer1':answer1, 'temp':temp})