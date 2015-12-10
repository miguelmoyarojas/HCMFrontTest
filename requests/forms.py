from django.forms import ModelForm
from .models import Vacant, Vacation

class VacantForm(ModelForm):
	class Meta:
		model = Vacant
		fields = [
			'requested_position',
			'vacants_amount',
			'position_type',
			'working_day_type',
			'salary',
			'comments',
			'request_date',
			'requested_by'
		]

	def __init__(self, *args, **kwargs):
		super(VacantForm, self).__init__(*args, **kwargs)
		self.fields['requested_position'].widget.attrs.update({'class': 'form-control'})
		self.fields['vacants_amount'].widget.attrs.update({'class': 'form-control'})
		self.fields['position_type'].widget.attrs.update({'class': 'form-control'})
		self.fields['working_day_type'].widget.attrs.update({'class': 'form-control'})
		self.fields['salary'].widget.attrs.update({'class': 'form-control'})
		self.fields['comments'].widget.attrs.update({'class': 'form-control'})
		self.fields['request_date'].widget.attrs.update({'class': 'form-control'})
		self.fields['requested_by'].widget.attrs.update({'class': 'form-control'})

class VacationForm(ModelForm):
	class Meta:
		model = Vacation
		fields = [
			'start_date',
			'end_date',
			'motive',
			'request_date',
			'requested_by',
			'assigned_to'
		]

	def __init__(self, *args, **kwargs):
		super(VacationForm, self).__init__(*args, **kwargs)
		self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
		self.fields['end_date'].widget.attrs.update({'class': 'form-control'})
		self.fields['motive'].widget.attrs.update({'class': 'form-control'})
		self.fields['request_date'].widget.attrs.update({'class': 'form-control'})
		self.fields['requested_by'].widget.attrs.update({'class': 'form-control'})
		self.fields['assigned_to'].widget.attrs.update({'class': 'form-control'})

class ApproveVacantForm(ModelForm):
	class Meta:
		model = Vacant
		fields = ['approved', 'assigned_to']

	def __init__(self, *args, **kwargs):
		super(ApproveVacantForm, self).__init__(*args, **kwargs)
		self.fields['approved'].widget.attrs.update({'class': 'form-control'})
		self.fields['assigned_to'].widget.attrs.update({'class': 'form-control'})