from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    
    if request.method =='GET':
        request.session['counter']+=1
        
    elif request.method == 'POST':
        request.session['counter']=1

    context = {
        'random_string': get_random_string(length=14)
    }
    return render(request, 'index2.html',context) 

def reset(request):
    request.session['counter']= 0
    return redirect('/random_word/')