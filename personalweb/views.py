from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
	template = 'inicio.html'
	context = {
		'languages': [
			{'value': 'en', 'name': 'English', 'data': 'langEn'},
			{'value': 'es', 'name': 'Spanish', 'data': 'langEs'},
		]
	}

	return render(request, template, context)


def escritor(request):
	return HttpResponse('Página de Escritor')
