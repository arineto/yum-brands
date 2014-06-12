from django.forms import ModelForm
from django import forms
from core.models import *

class BranchForm(ModelForm):
	class Meta:
		model = Branch
		exclude = ('latitude', 'longitude')

	def __init__(self, *args, **kwargs):
		super(BranchForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({'class' : 'form-control'})
		self.fields['franchise'].widget.attrs.update({'class' : 'form-control'})
		self.fields['contact_name'].widget.attrs.update({'class' : 'form-control'})
		self.fields['phone'].widget.attrs.update({'class' : 'form-control'})
		self.fields['email'].widget.attrs.update({'class' : 'form-control'})
		self.fields['owner_name'].widget.attrs.update({'class' : 'form-control'})
		self.fields['operator_name'].widget.attrs.update({'class' : 'form-control'})
		self.fields['address'].widget.attrs.update({'class' : 'form-control'})