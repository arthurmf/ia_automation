from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ActivityForm

# Create your views here.
def index(request):
    #audit_types = Type.objects.all()
    return render(request, "project/Activities_Dashboard.html")

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
            return HttpResponseRedirect("feliz")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ActivityForm()

    return render(request, 'project/new.html', {'form': form})