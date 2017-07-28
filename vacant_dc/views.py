from django.shortcuts import render
from mapbox import Datasets
import json  

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from django.views.generic import TemplateView


class IndexView(TemplateView):
	template_name = 'vacant_dc/index.html'

class FormView(TemplateView):
	template_name = 'vacant_dc/form.html'

# class QueryResults():
# 	token = os.environ.get('MAPBOX_ACCESS_TOKEN', False)
# 	if not token:
# 		print('environment variable MapboxAccessToken must be set')
# 		sys.exit(1)
# 	resp = urlopen('https://api.tiles.mapbox.com/geocoding/v5/mapbox.places/{query}.json?access_token={token}'.format(query=quote_plus(query), token='mapbox_access_token'))
# 	json.loads(resp.read().decode('utf-8'))
