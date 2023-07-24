from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form':form})

