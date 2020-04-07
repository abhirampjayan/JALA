from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewsForm
from .models import News

import pyreadstat
import pickle
import pandas as pd
# Create your views here.
def fakehome(request):
    if request.method=='POST':
        frm=NewsForm(request.POST)
        if frm.is_valid():
            text=frm.cleaned_data.get('text')
            m=frm.save()
            df , meta = pd.read_spss('final_model.sav')
            prediction = df.predict([var])
            prob = df.predict_proba([var])

            return HttpResponse("The given statement is ",prediction[0],"The truth probability score is ",prob[0][1])
    else:
        frm=NewsForm()
    return render(request,'fake/index.html',{'formfake':frm})
def result(request):
    context={'news':News.objects.all().order_by('id').reverse()}
    return render(request,'fake/result.html',context)

