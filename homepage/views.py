from django.shortcuts import render
from django.template import loader
# Create your views here.
def index(request):
    template = loader.get_template('homepage/index.html')
    return render(request,'homepage/index.html')

def response(request):
    template = loader.get_template('homepage/response.html')
    return render(request,'homepage/response.html')
