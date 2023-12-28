import base64
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import*
from .models import*
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def envoi(request):

    if request.method == 'POST':

        data = request.POST

        data = dict(data)

        data = {key:value[0] for key, value in data.items()}

        data = json.dumps(data)

        data = json.loads(data)
            
        json_data = json.dumps(data)

        encoded_data = base64.urlsafe_b64encode(json_data.encode()).decode()

        return HttpResponseRedirect(('/confirmation') + f'?data={encoded_data}')

    return render(request, 'patient.html')

    
    
def confirmation(request):

    encoded_data = request.GET.get('data')
    
    decoded_data = base64.urlsafe_b64decode(encoded_data).decode()

    data = json.loads(decoded_data)

    data = json.dumps(data)

    data = json.loads(data)

    person = {}

    tmp = {}

    for key, value in data.items():
        tmp[key] = value
        person = (tmp)


    return render(request,'confirmation.html', context={"data" : person})
