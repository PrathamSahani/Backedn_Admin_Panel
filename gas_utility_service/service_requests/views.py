from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def request_tracking(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'request_tracking.html', {'requests': requests})
