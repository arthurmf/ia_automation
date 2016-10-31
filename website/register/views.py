from django.shortcuts import redirect, render
from .forms import ClientEmployeeUserForm, ClientEmployeeForm, EyEmployeeUserForm, EyEmployeeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Client_employee, Ey_employee

# Create your views here.
def register_ClientEmployee_part1(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #print post.id
            #return HttpResponseRedirect("register_ClientEmployee_part2")
            return redirect('register_ClientEmployee_part2', perfil_id=post.id)
    else:
        form = UserCreationForm()
    return render(request, 'register/register_client_employee1.html', {'form': form})

def register_ClientEmployee_part2(request, perfil_id):
    user = User.objects.get(id=perfil_id)
    if request.method == 'POST':
        user_form = ClientEmployeeUserForm(request.POST)
        client_form = ClientEmployeeForm(request.POST)
        #client_form.fields['client_user'].widget = forms.HiddenInput()
        #client_form.client_user = perfil_id 
        #print "client_form.client_user --> " + str(client_form.client_user)
        
        print user_form.is_valid()        
        
        if user_form.is_valid():
            print "form vaido!!!"
            post_user_form = user_form.save(commit=False)
            user.first_name = post_user_form.first_name
            user.last_name = post_user_form.last_name
            user.email = post_user_form.email
            user.is_superuser = post_user_form.is_superuser
            user.is_staff = post_user_form.is_staff 
            user.is_active  = post_user_form.is_active  
            user.date_joined  = post_user_form.date_joined  
            user.save()
            post_client_form = client_form.save(commit=False)
            userx = User.objects.get(id=perfil_id)
            #post_client_form.client_user = userx.id
            Client_employee(client_position = post_client_form.client_position,
                            client = post_client_form.client,
                            client_employee_telephone = post_client_form.client_employee_telephone,
                            client_user = userx).save()
            #post_client_form.save()
            #return HttpResponseRedirect("feliz")
            return redirect("index")
    else:
        user_form = ClientEmployeeUserForm()
        client_form = ClientEmployeeForm()
        client_form.fields['client_user'].widget = forms.HiddenInput()
        #client_form.client_user = perfil_id
        
    return render(request, 'register/register_client_employee2.html', {'user_form': user_form, 'client_form': client_form})
    #return render(request, 'register/register_client_employee2.html', {'user_form': user_form})

def register_EyEmployee_part1(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            #print post.id
            #return HttpResponseRedirect("register_ClientEmployee_part2")
            return redirect('register_EyEmployee_part2', perfil_id=post.id)
    else:
        form = UserCreationForm()
    return render(request, 'register/register_client_employee1.html', {'form': form})

def register_EyEmployee_part2(request, perfil_id):
    user = User.objects.get(id=perfil_id)
    if request.method == 'POST':
        user_form = EyEmployeeUserForm(request.POST)
        client_form = EyEmployeeForm(request.POST)
        #client_form.fields['client_user'].widget = forms.HiddenInput()
        #client_form.client_user = perfil_id 
        #print "client_form.client_user --> " + str(client_form.client_user)
        
        print user_form.is_valid()        
        
        if user_form.is_valid():
            print "form vaido!!!"
            post_user_form = user_form.save(commit=False)
            user.first_name = post_user_form.first_name
            user.last_name = post_user_form.last_name
            user.email = post_user_form.email
            user.is_superuser = post_user_form.is_superuser
            user.is_staff = post_user_form.is_staff 
            user.is_active  = post_user_form.is_active  
            user.date_joined  = post_user_form.date_joined  
            user.save()
            post_client_form = client_form.save(commit=False)
            #post_client_form.client_user = int(perfil_id)
            #post_client_form.save()
            userx = User.objects.get(id=perfil_id)
            Ey_employee(ey_position = post_client_form.ey_position,
                ey_employee_telephone = post_client_form.ey_employee_telephone,
                ey_employee_user = userx).save()
            #return HttpResponseRedirect("feliz")
            return redirect("index")
    else:
        user_form = EyEmployeeUserForm()
        client_form = EyEmployeeForm()
        client_form.fields['ey_employee_user'].widget = forms.HiddenInput()
        #client_form.client_user = perfil_id
        
    return render(request, 'register/register_client_employee2.html', {'user_form': user_form, 'client_form': client_form})
    #return render(request, 'register/register_client_employee2.html', {'user_form': user_form})
