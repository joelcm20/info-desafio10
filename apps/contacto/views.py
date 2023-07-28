from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if not form.is_valid():
            return render(request, "contacto.html", {
                "form": ContactoForm,
                "error": "Los datos son invalidos."
            })
        form.save()
        return render(request, "contacto.html", {"form": ContactoForm, "msg": "Mensaje enviado!"})

    return render(request, "contacto.html", {"form": ContactoForm})
