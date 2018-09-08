# my_site/views.py

#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from django.template.context_processors import csrf
from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import PortfolioItem, Category
from .forms import ContactsForm

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

def about_page(request):
    return render(request, 'pages/about.html', {
        'categories': Category.objects.all()
    })


def home_page(request):
    return render(request, 'pages/index.html', {
        'title': 'Home page'
    })


def frontend_page(request):
    works = PortfolioItem.objects.all()
    paginator = Paginator(works, 6) # Show 6 works per page
    page = request.GET.get('page')
    works = paginator.get_page(page)

    return render(request, 'pages/frontend.html', {
        'title': 'Portfolio frontend page',
        'works': works
    })


def backend_page(request):
    return render(request, 'pages/backend.html', {
        'title': 'Portfolio backend page'
    })


def other_page(request):
    return render(request, 'pages/other.html', {
        'title': 'Portfolio other page'
    })


def info_page(request):
    return render(request, 'pages/info.html', {})


def services_page(request):
    return render(request, 'pages/services.html', {})



def contacts_page(request):
    args = {}
    args.update(csrf(request))
    args['form'] = ContactsForm

    if request.POST:
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/feedback.html', { 'name': form.cleaned_data['name'] })
    else:
        form = ContactsForm()
        return render(request, 'pages/contacts.html', args)




def work_page(request, pk):
    return render(request, 'pages/work.html', {
        'works': PortfolioItem.objects.all(),
        'work': get_object_or_404(PortfolioItem, pk=pk)
    })