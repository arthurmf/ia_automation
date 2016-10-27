from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ActivityForm, Template_Upload
from project.models import Activity
from documents.models import Request, Received
from django.core.mail import send_mail
from documents.models import Template, Request
from documents.forms import EmailForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.template import Context
from django.utils.safestring import mark_safe
from website.settings import BASE_DIR
from status.models import Workflow
from django.conf import settings
from django.core.files.storage import FileSystemStorage 

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

def handle_uploaded_file(f):
    with open('C:/Users/Eric.Boury/Desktop/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
  
            
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
            #for i in range(0, len(email_variable)):
            #    message.append(template_list[i].template_name)
            
            subject = "Email de teste django"
            from_email = "ia.automation.tool@gmail.com"
            to = email
            message = get_template(email_page).render(Context({'template_list': template_list, 'BASE_DIR' : BASE_DIR}))
            msg = EmailMessage(subject, mark_safe(message), to=[to], from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()
            #html_message = loader.render_to_string('project/email.html', {'message': message})
            #send_mail(subject, "X", from_email, [to], fail_silently=False, html_message=html_message)
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
    #return next_status
            
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
    act = Activity.objects.get(id=perfil_id)
    status_check = act.status
    options = {1: step_one,
               2: step_two,}
    

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
        next_status = update_status(perfil_id, "success")
        #current_project = Activity.objects.get(id=perfil_id)
        #current_project.status_id = next_status
        #current_project.save()
        Request(activity_id=perfil_id,
				client_employee_id=1,
				ey_employee_id=1,
				template_id=1).save()
        return render(request, 'project/email_sender.html', {'activity':teste,'templates': templates, 'form': form})
    else:
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
    upload_form = Template_Upload()
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        sending_email(mail_recipient_list, myfile, 'project/email_step2.html')
        
        Received(received_name = req_object.template.template_name, 
                 received_description = req_object.template.template_description,
                 received_format = req_object.template.template_format,
                 received_version = req_object.template.template_version,
                 received_path = req_object.template.template_path,
                 activity = teste,
                 client_employee = req_object.client_employee,
                 ey_employee = req_object.ey_employee,
                 template = req_object.template).save()
        next_status = update_status(perfil_id, "success")
        #teste.status_id = next_status
        #teste.save()
        return render(request, 'project/Project_Details_Step2_Success.html', {
            'uploaded_file_url': uploaded_file_url
        })
        print "Esse é o Branch do Eric"
    return render(request, 'project/Project_Details_Step2.html', {'activity':teste, 'documents':req, 'upload_form':upload_form})
    #except:
        #return render(request, 'project/Project_Details_Step2_N.html', {'activity':teste, 'documents':req})