# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from loyalty.forms import RegistrationForm
def index(request):
    template = "index.html"
    form = RegistrationForm()
    return render_to_response(template,{"form" :form},context_instance=RequestContext(request))
