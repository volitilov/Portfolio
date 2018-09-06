from django.template.context_processors import csrf
from django.shortcuts import render, get_object_or_404

from .models import PortfolioItem, Category
from .forms import ContactsForm



# About page :::::::::::::::::::::::::::::::::::::::::::::
def about(request):
	categories = Category.objects.all()
	return render(request, 'pages/about.html', {'categories': categories})


# Home page :::::::::::::::::::::::::::::::::::::::::
def home(request):
	data = {
		'works': PortfolioItem.objects.all(),
	}
	
	return render(request, 'pages/index.html', data)


# Info page ::::::::::::::::::::::::::::::::::::::::::::::
def info(request):
	return render(request, 'pages/info.html', {})


# Services page ::::::::::::::::::::::::::::::::::::::::::
def services(request):
	return render(request, 'pages/services.html', {})


# Contacts page ::::::::::::::::::::::::::::::::::::::::::
def contacts(request):
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



# Work page ::::::::::::::::::::::::::::::::::::::::::::::
def work(request, pk):
	data = {
		'works': PortfolioItem.objects.all(),
		'work': get_object_or_404(PortfolioItem, pk=pk)
	}

	return render(request, 'pages/work.html', data)