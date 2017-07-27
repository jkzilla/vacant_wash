from django.shortcuts import render
from mapbox import Datasets



def index(request):
	
	context = {}
	return render(request, 'vacant_dc/index.html', context)
