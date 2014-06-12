from django.forms import ModelForm
from django import forms
from core.models import *

class BranchForm(ModelForm):
	class Meta:
		model = Branch
		exclude = ('latitude', 'longitude')

	def __init__(self, *args, **kwargs):
		super(BranchForm, self).__init__(*args, **kwargs)
		self.fields['brand'].widget.attrs.update({'class' : 'form-control'})
		self.fields['address'].widget.attrs.update({'class' : 'form-control'})