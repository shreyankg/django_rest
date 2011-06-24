# Create your views here.
from django.shortcuts import render_to_response
from models import Soap, SoapForm

def index(request):
    if request.method == 'POST':
        soap = SoapForm(request.POST)
        soap.save()
    soaps = Soap.objects.all()
    return render_to_response(
        'index.html', 
        {
            'soaps':  soaps
        }
    )

def show(request, soap_id):
    soap = Soap.objects.get(id=soap_id)
    if request.method == 'PUT':
        f = SoapForm(request.POST, instance=soap)
        f.save()
        soap = Soap.objects.get(id=soap_id)
    return render_to_response(
        'show.html', 
        {
            'soap':  soap
        }
    )

def new(request):
    soap_form = SoapForm()
    return render_to_response(
        'new.html', 
        {
            'soap_form':  soap_form
        }
    )

def edit(request, soap_id):
    soap = Soap.objects.get(id=soap_id)
    soap_form = SoapForm(instance=soap)
    return render_to_response(
        'edit.html', 
        {
            'soap': soap,
            'soap_form':  soap_form
        }
    )


