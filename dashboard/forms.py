from django import forms
from Portfolio.models import Information, Project



class EditProfileForm(forms.ModelForm):
	
	class Meta:
		model = Information
		exclude = ('born_date', 'address', 'cv')

class CreateProjectForm(forms.ModelForm):

	class Meta:
		model = Project
		exclude = ('Slug',)
