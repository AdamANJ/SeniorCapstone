from django.shortcuts import render
from personal.models import (
	textContainer,
	imageContainer,
	Speaker,
	Highlighted_Speaker,
	registration,
	events
)
from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.

def home_screen_view(request):

	context = {}

	text = textContainer.objects.all()
	context['text'] = text

	image = imageContainer.objects.all()
	context['image'] = image

	speaker = Highlighted_Speaker.objects.all()
	context['speaker'] = speaker

	register = registration.objects.all()
	context['register'] = register

	event = events.objects.all()
	context['events'] = event

	return render(request, "personal/home.html", context)

def speakers_view(request):

	context= {}

	speaker = Speaker.objects.all()
	context['speaker'] = speaker	

	return render(request, "personal/speakers.html", context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RegistrationForm()
    
    return render(request, 'personal/registration.html', {'form': form})

def success(request):

	context= {}

	return render(request, "personal/success.html", context)