from django.http import Http404
from django.shortcuts import render
from main.models import *
#from main.templates import *
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import *
from django.shortcuts import render
#from django.core.context_processor import csrf
#from django.views.decorators.csrf import csrf_exmpt
from datetime import *
import random
import string

# Create your views here.
def home(request):
	
	category = Category.objects.all()
	context = {
	       'sitename': 'Интернет-магазин',
	       'categories': category,
	}
	return HttpResponse(render_to_string('home.html', context))


def item(request, alias):
	try:
		tovar = Items.objects.get(alias=alias)
	except:
		raise Http404('Объект не найден!')

	
	context = {
	       'tovar': tovar,
	}
	return HttpResponse(render_to_string('item.html', context))


def get_category(request, alias):
	try:
		category = Category.objects.get(alias=alias)
		tovars = Items.objects.filter(category=category)
	except:
		raise Http404('Объект не найден!')
	
	context = {
	       'tovars': tovars,
	       'category': category,
	}
	return HttpResponse(render_to_string('index.html', context))

