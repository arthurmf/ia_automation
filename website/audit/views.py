from django.shortcuts import render
from .models import Type

def index(request):
    audit_types = Type.objects.all()
    return render(request, "audit/Activities_Dashboard.html", {'audit_types': audit_types})
    