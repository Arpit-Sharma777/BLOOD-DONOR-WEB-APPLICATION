from django.shortcuts import render, redirect
from .models import Donor, BloodRequest
from .forms import DonorForm, BloodRequestForm

def donor_register(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']

            if int(weight) < 50:
                weight_info = "Weight should be greater than or equal to 50 kg"
                return render(request, 'donor/donor_form.html', {'form': form, 'weight_info': weight_info})

            if int(weight) > 150:
                weight_info = "Weight should not exceed 150 kg"
                return render(request, 'donor/donor_form.html', {'form': form, 'weight_info': weight_info})

            if int(age) < 18:
                age_info = "You must be at least 18 years old to use this application."
                return render(request, 'donor/donor_form.html', {'form': form, 'age_info': age_info})

            form.save()
            return redirect('donor_list')
    else:
        form = DonorForm()
    return render(request, 'donor/donor_form.html', {'form': form})

from django.shortcuts import render, redirect

def home_view(request):
    return render(request, 'donor/index.html')

def blood_request(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save()
            # You can add logic to handle the blood request here
            return redirect('blood_request_success')
    else:
        form = BloodRequestForm()
    return render(request, 'donor/blood_request_form.html', {'form': form})

def donor_list(request):
    blood_group = request.GET.get('blood_group')
    location = request.GET.get('location')
    donors = Donor.objects.all()
    if blood_group:
        donors = donors.filter(blood_group=blood_group)
    if location:
        donors = donors.filter(city__icontains=location)
    return render(request, 'donor/donor_list.html', {'donors': donors})