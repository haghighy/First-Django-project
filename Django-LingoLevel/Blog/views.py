from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def introduction(request):
    if request.method=="GET":
        print("{}".format(request.method))
        return render(request, "introduction.html")
    if request.method=="POST":
        return render(request, "form.html")


def form(request):
    if request.method=="GET":
        print("{}".format(request.method))
        return render(request, "form.html")
    if request.method=="POST":
        # model=User.objects.create(fname=request.POST["fname"],lname=request.POST["lname"],v1=request.POST["v1"],v2=request.POST["v2"],v3=request.POST["v3"],v4=request.POST["v4"],v5=request.POST["v5"],v6=request.POST["v6"],v7=request.POST["v7"],v8=request.POST["v8"],v9=request.POST["v9"],v10=request.POST["v10"],v11=request.POST["v11"],v12=request.POST["v12"],g1=request.POST["g1"],g2=request.POST["g2"],g3=request.POST["g3"],g4=request.POST["g4"],g5=request.POST["g5"],g6=request.POST["g6"],g7=request.POST["g7"],g8=request.POST["g8"],g9=request.POST["g9"],g10=request.POST["g10"],l1=request.POST["l1"],l2=request.POST["l2"],l3=request.POST["l3"],l4=request.POST["l4"],l5=request.POST["l5"],l6=request.POST["l6"],l7=request.POST["l7"],l8=request.POST["l8"])
        
        score=0
        v5=request.POST["v5"]
        if v5=='able':
            score+=2
        if request.POST["v1"]=='My':
            score+=1
        if request.POST["v2"]=='expensive':
            score+=1
        if request.POST["v3"]=='noisy':
            score+=1
        if request.POST["v4"]=='wear':
            score+=2
        if request.POST["v6"]=='at':
            score+=2
        if request.POST["v7"]=='getting':
            score+=3
        if request.POST["v8"]=='before':
            score+=3
        if request.POST["v9"]=='managed to':
            score+=3
        if request.POST["v10"]=='wish':
            score+=3
        if request.POST["v11"]=='sort out':
            score+=3
        if request.POST["v12"]=='offered':
            score+=3
        if request.POST["g1"]=='Where':
            score+=1
        if request.POST["g2"]=='There’s':
            score+=1
        if request.POST["g3"]=='dark, long':
            score+=1
        if request.POST["g4"]=='speak':
            score+=2
        if request.POST["g5"]=='So':
            score+=2
        if request.POST["g6"]==' to be':
            score+=2
        if request.POST["g7"]=='worse':
            score+=3
        if request.POST["g8"]=='hard':
            score+=3
        if request.POST["g9"]=='easily':
            score+=3
        if request.POST["g10"]=='by':
            score+=3
        if request.POST["l1"]=='False':
            score+=1
        if request.POST["l2"]=='True':
            score+=1
        if request.POST["l3"]=='digest food.':
            score+=2
        if request.POST["l4"]=='eyelashes':
            score+=2
        if request.POST["l5"]=='True':
            score+=3
        if request.POST["l6"]=='False':
            score+=3
        if request.POST["l7"]=='False':
            score+=3
        if request.POST["l8"]=='True':
            score+=3
        model=User.objects.create(score=score,fname=request.POST["fname"],lname=request.POST["lname"],v1=request.POST["v1"],v2=request.POST["v2"],v3=request.POST["v3"],v4=request.POST["v4"],v5=request.POST["v5"],v6=request.POST["v6"],v7=request.POST["v7"],v8=request.POST["v8"],v9=request.POST["v9"],v10=request.POST["v10"],v11=request.POST["v11"],v12=request.POST["v12"],g1=request.POST["g1"],g2=request.POST["g2"],g3=request.POST["g3"],g4=request.POST["g4"],g5=request.POST["g5"],g6=request.POST["g6"],g7=request.POST["g7"],g8=request.POST["g8"],g9=request.POST["g9"],g10=request.POST["g10"],l1=request.POST["l1"],l2=request.POST["l2"],l3=request.POST["l3"],l4=request.POST["l4"],l5=request.POST["l5"],l6=request.POST["l6"],l7=request.POST["l7"],l8=request.POST["l8"])
        
        listscore=[score]
        context={"data":listscore}
        # context={}
        
        context["score"]=score
        context["Firstname"]=request.POST["fname"]
        context["Lastname"]= request.POST["lname"]
        return render(request, "result.html", context= context)



# def modernform(request):
    # if request.method == "GET":
        # return render(request, "modernform.html")

