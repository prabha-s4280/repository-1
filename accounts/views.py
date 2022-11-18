from django.shortcuts import render
def home_view(request):
    context={
        'first':'prabhas','last':'sunnam'
    }
    return render(request,'index.html',context)