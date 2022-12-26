from django.shortcuts import render

# Create your views here.
def sree(request):
    p={'name':'sree'}
    return render(request,'sree.html',p)
