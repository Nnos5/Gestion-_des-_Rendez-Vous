from django.shortcuts import render,redirect
from django.http import HttpRequest
from app1.forms import*


# Create your views here.
def envoi(request):
    if request=='POST':
        formulaire = FormDonnee(request.POST)
        if formulaire.is_valid():
            donne = formulaire.save(commit=False)
            donne.save
            return redirect('message',pk = donne.pk)
    else:
        formulaire=FormDonnee()

    return render(request,'personnel/patient.html',{'formulaire':formulaire})
            

    

def message(request,pk):
    donnee = Donnee.objects.get(pk=pk)
    if request.method =='POST':
        formulaire = FormRdv(request.POST)
        if formulaire.is_valid():
            donnee2 = formulaire.save(commit=False)
            donnee2 = donnee
            donnee2.save()
            return redirect('Confirmation')
    else:
        formulaire = FormRdv(initial={'donnee':donnee})

    return render(request,'personnel/Rendezvous.html',{'formulaire':formulaire})


def confirmation(request):
    return render(request,'personnel/confirmation.html')

 
