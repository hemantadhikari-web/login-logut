from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
from home.models import Contact

#define karo variable fir usme jo naam ka template chahye uska naam daal do request karo basically
#aur fir jab wo file agyi tum usme changes daal do
def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request,'index.html',context)
def about(request):
    #return HttpResponse("this is aboutpage")
    return render(request,'about.html')
def services(request):
    #return HttpResponse("this is servicespage")
    return render(request,'services.html')
def contact(request):
    if request.method=="POST":
        name =request.POST.get('name')
        phone =request.POST.get('phone')
        email =request.POST.get('email')
        desc =request.POST.get('desc')
        contact = Contact(name = name, email = email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'your msg has been sent')
    return render(request,'contact.html')

# Create your views here.
