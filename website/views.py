from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})


def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']


		# send an email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from
			['esengazypakiza@gmail.com'], # to
			)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})


def about(request):
	return render(request, 'about.html', {})

def price(request):
	return render(request, 'price.html', {})

def service(request):
	return render(request, 'service.html', {})


def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-date']


		appointment = "Name: " + your_name  + " Email: " + your_email + " Schedule: " + your_schedule + " Day: " + your_date 

		send_mail(
			'Appointment Request', # subject
			appointment, # message
			your_email, # from email
			['kimgrishulya@gmail.com'], # To Email
			)
		
		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_email': your_email,
			'your_schedule': your_schedule,
			'your_date': your_date
			})

	else:
		return render(request, 'home.html', {})