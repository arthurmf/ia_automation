from .forms import NewDocumentForm
from django.shortcuts import render
from register.models import Ey_employee

def new_document(request):
    form = NewDocumentForm()
    return render(request, 'documents/new_document.html', {'form': form})
