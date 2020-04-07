from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewsForm
from .models import News
# Create your views here.
def fakehome(request):
    if request.method=='POST':
        frm=NewsForm(request.POST)
        if frm.is_valid():
            m=frm.save()
            return redirect('result')
    else:
        frm=NewsForm()
    return render(request,'fake/index.html',{'formfake':frm})
def result(request):
    context={'news':News.objects.all().order_by('id').reverse()}
    return render(request,'fake/result.html',context)