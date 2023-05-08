from django.shortcuts import render

# Create your views here.

def ProductRead(request):
    data = Product.objects.all()
    return render(request,'read.htm',{'data':data})
