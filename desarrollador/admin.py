from django.contrib import admin
from .models import About, Project, Skill, Contact
from parler.admin import TranslatableAdmin

# About model
class AboutAdmin(admin.ModelAdmin):
    list_display = ("about", "created",)
    list_filter = ("created",)
    date_hierarchy = "created"

class TranslatedAboutAdmin(AboutAdmin, TranslatableAdmin):
    pass

admin.site.register(About, TranslatedAboutAdmin)


# Project model
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "link",)
    search_fields = ("name",)
    list_per_page = 25

class TranslatedProjectAdmin(ProjectAdmin, TranslatableAdmin):
    pass

admin.site.register(Project, TranslatedProjectAdmin)


# Skill model
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "image",)
    list_per_page = 25

class TranslatedSkillAdmin(SkillAdmin, TranslatableAdmin):
    pass

admin.site.register(Skill, TranslatedSkillAdmin)


# Contact model
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "image",)

class TranslatedContactAdmin(ContactAdmin, TranslatableAdmin):
    pass

admin.site.register(Contact, TranslatedContactAdmin)
