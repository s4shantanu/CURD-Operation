from django.shortcuts import render
from .forms import Studentregistration
from .models import User

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = Studentregistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em)
            reg.save()
            fm = Studentregistration()
    else:
        fm = Studentregistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})
