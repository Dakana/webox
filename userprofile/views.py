from django.shortcuts import render
from .forms import UserCreationEmailForm
from .forms import EmailAuthenticationForm
# Create your views here.

def signup(request):
  form=UserCreationEmailForm(request.POST or None)

  if form.is_valid():
    form.save()


  return render(request,'signup.html',{'form':form})

def signin(request):
  form = EmailAuthenticationForm(request.POST or None)

  #if form.is_valid()
    #login

  return render(request,'singin.html'),{'form':form}
