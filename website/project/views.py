# -*- coding: utf-8 -*-
# Libs de Django
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context
from django.utils.safestring import mark_safe
from django.core.files.storage import FileSystemStorage 
# Libs de Settings
from website.settings import BASE_DIR
# Libs de forms
from .forms import ActivityForm, Validation_Form
from documents.forms import EmailForm
# Libs de models
from documents.models import Request, Received, Template
from project.models import Activity
from status.models import Workflow


# Create your views here.
def index(request):
    if request.method == 'POST':        
        return HttpResponseRedirect("new")
    else:
        return render(request, 'project/Activities_Dashboard.html', {'activity': Activity.objects.all()})
    
def new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ActivityForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.save()
            #return HttpResponseRedirect("feliz")
            return redirect("index")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ActivityForm()
    return render(request, 'project/new.html', {'form': form})


def sending_email(email_variable, template_list, email_page):
    print email_variable
    try:
        email_list = email_variable[0].split(";")           
    except:
        email_list = []
        print "Deu ruim 1 ..."
    for email in email_list:
        print email_list
        if "@" in email:
            message = []           
            subject = "Email de teste django"
            from_email = "ia.automation.tool@gmail.com"
            to = email
            message = get_template(email_page).render(Context({'template_list': template_list, 'BASE_DIR' : BASE_DIR}))
            msg = EmailMessage(subject, mark_safe(message), to=[to], from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()
        else:
            print "Deu ruim 2 ..."

def update_status(project_id, choice):
    current_project = Activity.objects.get(id=project_id) 
    current_status = current_project.status_id
    current_workflow = Workflow.objects.get(workflow_current_status=current_status)
    
    if choice == 'success':        
        next_status = current_workflow.workflow_success_next_status
        print str(current_status) + " --> " + str(next_status)
    elif choice == 'fail':        
        next_status = current_workflow.workflow_fail_next_status
        print str(current_status) + " --> " + str(next_status)
    else:
        print "deu ruim..."
    
    current_project.status_id = next_status
    current_project.save()
    return "Status alterado de: " + str(current_status) + " para: " + str(next_status)
            
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'project/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'project/upload.html')

            
def step(request, perfil_id):
    #Método destinado ao controle de passos do workflow
    act = Activity.objects.get(id=perfil_id)
    status_check = act.status
    options = {1: step_one,
               2: step_two,
               3: step_three,}

    return HttpResponse(options[status_check.id](request, perfil_id));
    
               
def step_one(request, perfil_id):
    print "STEP 1"
    Request.objects.filter(activity_id=perfil_id).delete()
    teste = Activity.objects.get(id=perfil_id)
    templates = Template.objects.all()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        email_body = []
        print len(form.data)        
        for i in range(1, (len(form.data) - 1)):
            email_body.append(form.data.get('email_field_' + str(i))) 
        sending_email(email_body, templates, 'project/email.html')
        update_status(perfil_id, "success")
        Request(activity_id=perfil_id,
				client_employee_id=1,
				ey_employee_id=1,
				template_id=1).save()
        return render(request, 'project/email_sender.html', {'activity':teste,'templates': templates, 'form': form})

        #return redirect("index")
    else:
        print "(ELSE)"
        form = EmailForm()
        
    return render(request, 'project/email_sender.html', {'activity':teste,'templates': templates, 'form': form})

def step_two(request, perfil_id):
    print "STEP 2"
    Received.objects.filter(activity_id=perfil_id).delete() 
    teste = Activity.objects.get(id=perfil_id)
    req = Request.objects.filter(activity__id=perfil_id)
    #try:
    req_object = Request.objects.get(activity__id=perfil_id)

    mail_recipient = req_object.ey_employee.ey_employee_email
    mail_recipient_list = []
    mail_recipient_list.append(mail_recipient)
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        myfile_list = []
        myfile_list.append(myfile)
        print myfile
        print myfile_list
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        sending_email(mail_recipient_list, myfile_list, 'project/email_step2.html')
        
        Received(received_name = req_object.template.template_name, 
                 received_description = req_object.template.template_description,
                 received_format = req_object.template.template_format,
                 received_version = req_object.template.template_version,
                 received_path = req_object.template.template_path,
                 activity = teste,
                 client_employee = req_object.client_employee,
                 ey_employee = req_object.ey_employee,
                 template = req_object.template).save()
        update_status(perfil_id, "success")
        return render(request, 'project/Project_Details_Step2_Success.html', {
            'uploaded_file_url': uploaded_file_url
        })
        
    return render(request, 'project/Project_Details_Step2.html', {'activity':teste, 'documents':req})
    #except:
        #return render(request, 'project/Project_Details_Step2_N.html', {'activity':teste, 'documents':req})

    
def step_three(request, perfil_id):
    print "STEP 3"
    validation = Validation_Form();
    teste = Activity.objects.get(id=perfil_id)
    req_list = []
    req = Request.objects.filter(activity=perfil_id)
    req_list = list(req)
    options = {}
    received_control = []
    not_received_control = 0
    for item in req_list:
        if Received.objects.filter(activity=item.activity,template=item.template):
            options[item.id] = 'Received'
            received_control.append("Received")
        else:
            received_control.append("Not Received")
            options[item.id] = 'Not Received'
            not_received_control = 1
    
    if request.method == 'POST':
        validation = Validation_Form(request.POST)
        data = validation['validate'].value()
        if data == "True":
            data_bool = True
        else:
            data_bool = False


        if data_bool == True:
            return render(request, 'project/Project_Details_Step2_Success.html', {'activity':teste, 'req_list': req_list, 'received_control':received_control, 'options':options, 'not_received_control':not_received_control})            
        else:
            print "FALSE"
            validation = Validation_Form()

    return render(request, 'project/Project_Details_Step3.html', {'activity':teste, 'req_list': req_list, 'received_control':received_control, 'options':options, 'not_received_control':not_received_control, 'validation':validation})