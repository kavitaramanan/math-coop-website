from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'coop/base.html')

def dark_index(request):
    return render(request, 'coop/base2.html')