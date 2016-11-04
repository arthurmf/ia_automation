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
from project.models import Activity, Activity_Client
from status.models import Workflow
from register.models import Client_employee, Ey_employee
from django.contrib.auth.models import User
from django.forms import models
from pandas import DataFrame

import os

# Create your views here.
def index(request):
    #if request.user.is_staff:
    if request.method == 'POST':
        return HttpResponseRedirect("new")
    else:
        #print request.user.id
        return render(request, 'project/Activities_Dashboard.html', {'activity': Activity.objects.all()})
        #print Ey_employee.objects.filter(ey_employee_user=request.user.id)
        #return render(request, 'project/Activities_Dashboard.html', {'activity': Activity.objects.get(id)})
    #else:
    #       return redirect('step_two')

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

def check_if_path_exists(path):
    if os.path.exists(path) == False:
        os.makedirs(path)

def sending_email(email, template_list, email_page):
    message = []
    subject = "Email de teste django"
    from_email = "ia.automation.tool@gmail.com"
    to = email
    message = get_template(email_page).render(Context({'template_list': template_list, 'BASE_DIR' : BASE_DIR}))
    msg = EmailMessage(subject, mark_safe(message), to=[to], from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

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

def file_received_verifier(request, options, not_received_control, doc_request):
    for item in doc_request:
        if Received.objects.filter(activity=item.activity,template=item.template):
            options[item.id] = 'Received'
        else:
            options[item.id] = 'Not Received'
            not_received_control = 1

def handle_uploaded_file(f,dyn_path):
    with open(os.path.join(BASE_DIR, 'media\\'+str(dyn_path)+str(f.name)), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
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
    activity = Activity.objects.get(id=perfil_id)
    templates = Template.objects.all()
    email_list = Activity_Client.objects.filter(activity_id=perfil_id)
    if request.method == 'POST':
        dropdown_list = request.POST.getlist("dropdown")
        df = DataFrame(zip(dropdown_list, templates))
        print df
        for email in set(dropdown_list):
            if "@" in email:
                filtered_templates =  list(df[df[0] == email][1])
                sending_email(email, filtered_templates, 'project/email.html')
                user_client_id = User.objects.get(email=email).id
                for template in filtered_templates:

                    client_emp_obj = Client_employee.objects.get(client_user_id=user_client_id)
                    ey_emp_obj = Ey_employee.objects.get(ey_employee_user_id=request.user.id)

                    try:
                        Request.objects.get(activity_id=perfil_id,
                            client_employee_id=Client_employee.objects.get(client_user_id=user_client_id).id,
                            ey_employee_id=Ey_employee.objects.get(ey_employee_user_id=request.user.id).id,
                            template_id=template.id,
                            send_counter=0)
                    except:
                        path_string = "/media/" + \
                                      str(activity.audit.id) + "." + str(activity.audit) + "/" + \
                                      str(activity.id) + "." + str(activity.project_name) + "/" + \
                                      "1.Documentos Recebidos" + "/" + \
                                      str(request.user.id) + "." + request.user.first_name + request.user.last_name + "/" + \
                                      str(client_emp_obj.id) + "." + User.objects.get(email=email).first_name + \
                                      User.objects.get(email=email).last_name + "/" + \
                                      str(template.id) + "." + template.template_name

                        Request(activity_id=perfil_id,
                            client_employee_id=Client_employee.objects.get(client_user_id=user_client_id).id,
                            ey_employee_id=Ey_employee.objects.get(ey_employee_user_id=request.user.id).id,
                            template_id=template.id,
                            send_counter=0,
                            request_path=path_string).save()

                        #check_if_path_exists(path_string)
                        check_if_path_exists(BASE_DIR.replace("\\""", "/") + path_string)
                        #print path_string

        update_status(perfil_id, "fail")
        print "feliz"
        return render(request, 'project/email_sender.html', {'activity':activity,'templates': templates, 'email_list': email_list})
        #return redirect("index")
    else:
        print "(ELSE)"
        return render(request, 'project/email_sender.html', {'activity':activity,'templates': templates, 'email_list': email_list})

def step_two(request, perfil_id):
    print "STEP 2"
    teste = Activity.objects.get(id=perfil_id)
    doc_request = Request.objects.filter(activity__id=perfil_id)
    doc_request = list(doc_request)
    options = {}
    not_received_control = 0
    #Verificação antes do POST de quais documentos já foram enviados pelo cliente
    file_received_verifier(request, options, not_received_control, doc_request)
    #try:
        #mail_recipient = req_object.ey_employee.ey_employee_user.email
        #mail_recipient_list = []
        #mail_recipient_list.append(mail_recipient)
    if request.method == 'POST':
        #Para cada item dentro de request, é montado o ID do botão (upload) pressionado.
        for req in doc_request:
            aux_myfile = req.id
            aux_mybutton = "mybutton_" + str(aux_myfile)
            req_object = req
            #Caso o botão (upload) pressionado seja correspondente com o POST, o upload do arquivo é realizado.
            if aux_mybutton in request.POST:
                
                if options[aux_myfile] != 'Received':
                    #Atribuição do documento selecionado para realizar Upload
                    myfile = request.FILES['myfile_'+str(aux_myfile)]
                    myfile_list = []
                    myfile_list.append(myfile)
                    #Variável temporária para definição de path dinâmico para armazenamento de arquivos (esta variável deverá recever o valor referente à lógica de criação de pastas no MYSQL)
                    dyn_path = ""
                    #Novo método de upload de arquivos
                    handle_uploaded_file(myfile,dyn_path)
                    #fs = FileSystemStorage()
                    #filename = fs.save(myfile.name, myfile)
                    #uploaded_file_url = fs.url(filename)
                    
                    
                    #Inclusão de linha contendo o arquivo recebido na tabela Received do MySQL
                    Received(received_name = req_object.template.template_name, 
                             received_description = req_object.template.template_description,
                             received_format = req_object.template.template_format,
                             received_version = req_object.template.template_version,
                             received_path = req_object.template.template_path,
                             activity = teste,
                             client_employee = req_object.client_employee,
                             ey_employee = req_object.ey_employee,
                             template = req_object.template).save()
                    update_status(perfil_id, "fail")
                    
                    #Para que a página seja recarregada com os valores de "Recebido" ou "Não Recebido", é necessário chamar novamente o método
                    file_received_verifier(request, options, not_received_control, doc_request)
                    
                    #sending_email(mail_recipient_list, myfile_list, 'project/email_step2.html')
                    
                    #return render(request, 'project/Project_Details_Step2_Success.html', {
                        #'uploaded_file_url': uploaded_file_url
                    #})
                    
    return render(request, 'project/Project_Details_Step2.html', {'activity':teste, 'documents':doc_request, 'options':options, 'not_received_control':not_received_control})
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
    
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        myfile_list = []
        myfile_list.append(myfile)
        print myfile
        print myfile_list
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        
        validation = Validation_Form(request.POST)
        data = validation['validate'].value()
        if data == "True":
            data_bool = True
        else:
            data_bool = False


        if data_bool == True:
            return render(request, 'project/Project_Details_Step2_Success.html', {'activity':teste, 'req_list': req_list, 'received_control':received_control, 'options':options, 'not_received_control':not_received_control, 'uploaded_file_url': uploaded_file_url})            
        else:
            print "FALSE"
            validation = Validation_Form()

    return render(request, 'project/Project_Details_Step3.html', {'activity':teste, 'req_list': req_list, 'received_control':received_control, 'options':options, 'not_received_control':not_received_control, 'validation':validation})