from django.shortcuts import render
#from django.utils.translation import gettext as _
from .models import About, Project, Skill, Contact


def desarrollador(request):
	template = 'desarrollador.html'
	
	about = About.objects.get(id=1)
	projects = Project.objects.all().order_by('-id')
	skills = Skill.objects.all()
	contacts = Contact.objects.all()
	context = {
		"about": about,
		"projects": projects,
		"skills": skills,
		"contacts": contacts,
	}
	
	return render(request, template, context)
	
	