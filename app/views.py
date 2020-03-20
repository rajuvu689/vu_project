from django.shortcuts import render, get_object_or_404,redirect
from .models import Contact
from django.views.generic import ListView,DetailView
from django.db.models import Q

# Create your views here.
# def home(request):
#     context = {
#         'contacts': Contact.objects.all()
#     }
#     return render (request, 'index.html',context)

    # def detail(request,id):
    #     context = {
    #         'contact': get_object_or_404(Contact, pk=id)
    #     }
    #     return render(request,'detail.html',context)


class HomePageView(ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'

class ContactDetailView(DetailView):
    template_name = 'detail.html'
    model = Contact
    context_object_name = 'contact'

def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Contact.objects.filter(
        Q(name__icontains=search_term) |
        Q(email__icontains=search_term) |
        Q(info__icontains=search_term) |
        Q(phone__icontains=search_term) 
        )
        context = {
            'search_term': search_term,
            'contacts': search_results
        }
        return render(request, 'search.html', context)
    else:
        return redirect('home')