from django import forms
from .models import *

class FormDonnee(forms.ModelForm):
    
    class Meta:
        model = Donnee
        fields = ['nom','prenom','email','sexe','age']

    widgets ={

           "nom":forms.TextInput(attrs={'class':'form-control','placeholder':'NOM',}),
            "prenom":forms.TextInput(attrs={'class':'form-control','placeholder':'PRENOM'}),
            "email":forms.EmailInput(attrs={'class':'form-control' ,'placeholder':'EMAIL'}),
            "sexe":forms.Select(attrs={'class':'form-control','placeholder':'SEXE'}),
            "age":forms.NumberInput(attrs={'class':'form-control' ,'placeholder':'AGE'}),
    }   


class FormRdv(forms.ModelForm):
    class Meta:
        model = RDV
        fields = ['Date','Heure']
        widgets={
            'donnee': forms.HiddenInput()
        }

    widgets ={

            "nom":forms.TextInput(attrs={'class':'form-control','placeholder':'NOM',}),
            "prenom":forms.TextInput(attrs={'class':'form-control','placeholder':'PRENOM'}),
            "email":forms.EmailInput(attrs={'class':'form-control' ,'placeholder':'AGE'}),
            "sexe":forms.Select(attrs={'class':'form-control','placeholder':'SEXE'}),
            "age":forms.NumberInput(attrs={'class':'form-control' ,'placeholder':'AGE'}),
            "Date":forms.DateInput(attrs={'class':'form-control' ,'placeholder':'DATE'}),
            "Heure":forms.TimeInput(attrs={'class':'form-control' ,'placeholder':'HEURE'}),

    }   