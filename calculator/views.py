from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def calculator(request):
	return render(request,'calculator/calci.html')

def operations(request):
	n1=request.POST['num1']
	n2=request.POST['num2']
	add=round((float(n1)+float(n2)),4)
	sub=float(n1)-float(n2)
	mul=float(n1)*float(n2)
	div=round((float(n1)/float(n2)),4)
	mod=round((float(n1)%float(n2)),4)
	return render(request,'calculator/calci.html',context={'add':add,'sub':sub,'mul':mul,'div':div,'mod':mod})