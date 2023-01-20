from django.db import models
from datetime import date
from parler.models import TranslatableModel, TranslatedFields


class About(TranslatableModel):
	translations = TranslatedFields(
        about = models.TextField(blank=False, null=False),
    )
	created = models.DateField(default=date.today)

	def __str__(self):
		return self.about

class Project(TranslatableModel):
	translations = TranslatedFields(
		name = models.CharField(max_length=255, null=False),
	)
	link = models.URLField(max_length=255, null=False)

	def __str__(self):
		return self.name

class Skill(TranslatableModel):
	translations = TranslatedFields(
		name = models.CharField(max_length=255, null=False),
	)
	image = models.ImageField(upload_to='static/images/skills')

	def __str__(self):
		return self.name

class Contact(TranslatableModel):
	translations = TranslatedFields(
		name = models.CharField(max_length=255, null=False),
	)
	link = models.CharField(max_length=255, null=False)
	image = models.ImageField(upload_to='static/images/contact')

	def __str__(self):
		return self.name

