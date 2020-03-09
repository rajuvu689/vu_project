from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'status':'working on the contact manager app',
        'age':'22'
    }
    return render (request, 'index.html',context)