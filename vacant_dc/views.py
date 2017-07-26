from django.shortcuts import render



def index(request):
    context = {}
    return render(request, 'vacant_dc/index.html', context)