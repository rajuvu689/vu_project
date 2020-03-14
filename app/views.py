from django.shortcuts import render, get_object_or_404
from .models import Contact

# Create your views here.
def home(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render (request, 'index.html',context)

    def detail(request,id):
        context = {
            'contact': get_object_or_404(Contact, pk=id)
        }
        return render(request,'detail.html',context)