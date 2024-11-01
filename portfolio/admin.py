from django.contrib import admin
from .models import Project, Experience, Education, Skill
from .forms import ExperienceForm, EducationForm

class ExperienceAdmin(admin.ModelAdmin):
    form = ExperienceForm

class EducationAdmin(admin.ModelAdmin):
    form = EducationForm

admin.site.register(Project)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Skill)