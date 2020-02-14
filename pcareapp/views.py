from django.shortcuts import render
from django.http import HttpResponse
from win10toast import ToastNotifier
import time

# Create your views here.

def home(request):
    return render(request,'base.html')
    
def home2(request):
    return render(request,'pages/home.html')
def index(request):
    return render(request,'pages/about.html')
def login(request):
    return render(request,'pages/login.html')
def contact(request):
    return render(request,'pages/contact.html')
def health(request):
    return render(request,'careyourself/healthy_diet.html')
def awareness(request):
    return render(request,'careyourself/awareness.html')
def exercises(request):
    return render(request,'careyourself/exercises.html')
def pbook(request):
    return render(request,'careyourself/pbooks.html')
def vitamins(request):
    return render(request,'careyourself/vitamins.html')
def mental(request):
    return render(request,'careyourself/mental.html')
def notification(request):
    return render(request,'customers/notification.html')
def message(request):
    return render(request,'customers/msg.html')
def message1(request):
    return render(request,'customers/msg1.html')
    # if request.method == "GET":
    #     mname = request.GET.get('mname','')
    #     h = request.GET.get('h','')
    #     m = request.GET.get('m','')
    #     s = request.GET.get('s','')
    # while True:
    #     current_time=time.strftime("%H:%M:%S")
    #     if current_time == "h:m:s".format(h,m,s):
    #         break
    #     else:
    #         pass
    # hr=ToastNotifier()
    # hr.show_toast("REMINDER","MEDICINE TIMEEE")

