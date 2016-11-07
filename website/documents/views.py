from .forms import NewDocumentForm
from django.shortcuts import render
from register.models import Ey_employee

def new_document(request):
    if request.method == 'POST':
        print request.POST
        form = NewDocumentForm(request.POST)
        post = form.save(commit=False)
        post.template_author = Ey_employee.objects.get(ey_employee_user_id=request.user.id)
        post.save()
        return render(request, 'documents/new_document.html', {'form': form})
    else:
        form = NewDocumentForm()
        return render(request, 'documents/new_document.html', {'form': form})
