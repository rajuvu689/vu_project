from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render (request, 'index.html',context)