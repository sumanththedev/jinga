from django.shortcuts import render

# Create your views here.
def jp(request):
    return render(request,'jp.html',context={'name':'data','we':'backend'})