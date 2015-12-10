# -*- encoding: utf-8 -*-

from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Vacant, Vacation, User
from .forms import VacantForm, ApproveVacantForm, VacationForm
from django.contrib.messages import constants as message_constants
MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
				message_constants.INFO: 'info',
				message_constants.SUCCESS: 'success',
				message_constants.WARNING: 'warning',
				message_constants.ERROR: 'danger',}

@login_required
def index(request, view_type=None):
	user = request.user

	if view_type == '1':
		dataset_vacants = Vacant.objects.filter(requested_by=user)
	elif view_type == '2':
		dataset_vacants = Vacant.objects.filter(assigned_to=user)
	else:
		dataset_vacants = Vacant.objects.all()
		
	dataset_vacations = Vacation.objects.all()

	context = {
		'user': user,
		'dataset_vacants': dataset_vacants,
		'dataset_vacations': dataset_vacations
	}

	return render(request, 'requests/index.html', context)

@login_required
def view_vacant(request, request_id):
	data = get_object_or_404(Vacant, pk=request_id)
	return render(request, 'requests/view_vacant.html', {'data': data})

@login_required
def view_vacation(request, request_id):
	data = get_object_or_404(Vacation, pk=request_id)
	return render(request, 'requests/view_vacation.html', {'data': data})

@login_required
def new_vacant(request):
	if request.method == "POST":
		form = VacantForm(request.POST)
		if form.is_valid():
			requested_position = request.POST['requested_position']
			vacants_amount = request.POST['vacants_amount']
			position_type = request.POST['position_type']
			working_day_type = request.POST['working_day_type']
			salary = request.POST['salary']
			comments = request.POST['comments']
			request_date = request.POST['request_date']
			requested_by = request.POST['requested_by']

			vacant = Vacant(
				requested_position = requested_position,
				vacants_amount = vacants_amount,
				position_type = position_type,
				working_day_type = working_day_type,
				salary = salary,
				comments = comments,
				request_date = request_date,
				requested_by = User.objects.get(id=request.POST['requested_by'])
			)

			vacant.save()
			messages.add_message(request, messages.INFO, 'Ingreso exitoso.')
			return redirect('/requests/')
	else:
		form = VacantForm()

	return render(request, 'requests/new_vacant.html', {'form': form})

@login_required
def new_vacation(request):
	if request.method == "POST":
		form = VacationForm(request.POST)
		if form.is_valid():
			start_date = request.POST['start_date']
			end_date = request.POST['end_date']
			motive = request.POST['motive']
			request_date = request.POST['request_date']
			requested_by = request.POST['requested_by']
			assigned_to = request.POST['assigned_to']

			vacation = Vacation(
				start_date = start_date,
				end_date = end_date,
				motive = motive,
				request_date = request_date,
				requested_by = User.objects.get(id=request.POST['requested_by']),
				assigned_to = User.objects.get(id=request.POST['assigned_to'])
			)

			vacation.save()
			messages.add_message(request, messages.INFO, 'Ingreso exitoso.')
			return redirect('/requests/')
	else:
		form = VacationForm()

	return render(request, 'requests/new_vacation.html', {'form': form})

@login_required
def delete_vacant(request, request_id):
	vacant = Vacant(id=request_id)
	vacant.delete()
	messages.add_message(request, messages.INFO, 'Borrado exitoso.')
	return redirect('/requests/')

@login_required
def delete_vacation(request, request_id):
	vacation = Vacation(id=request_id)
	vacation.delete()
	messages.add_message(request, messages.INFO, 'Borrado exitoso.')
	return redirect('/requests/')

@login_required
def approve_vacant(request, request_id):
	if request.method == "POST":
		form = ApproveVacantForm(request.POST)

		if form.is_valid():
			vacant = Vacant.objects.get(pk=request_id)
			vacant.approved = request.POST['approved']
			vacant.assigned_to = User.objects.get(id=request.POST['assigned_to'])
			vacant.save()

			messages.add_message(request, messages.INFO, 'Aprobada y asignada.')
			return redirect('/requests/')
	else:
		form = ApproveVacantForm()

	return render(request, 'requests/approve_vacant.html', {'form': form, 'request_id': request_id})

@login_required
def login_view(request):
	user = authenticate(username=request.POST['username'], password=request.POST['password'])
	if user is not None:
		if user.is_active:
			login(request, user)
			return redirect('/requests/index/')
		else:
			return redirect('/requests/login/')
	else:
		return redirect('/requests/login/')

@login_required
def logout_view(request):
	logout(request)
	return redirect('/requests/login/')