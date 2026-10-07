from django.shortcuts import redirect, render
from django.urls import reverse
from .models import MenuItem
from .forms import ContactForm

# Create your views here.

def home(request):
    items = MenuItem.objects.all()
    return render(request, 'cafe/index.html', {'items': items})
def menu(request):
    items= MenuItem.objects.all().order_by('category')
    return render(request, 'cafe/menu.html', {'items':items})
def about(request):
    return render(request, 'cafe/about.html')
def contact(request):
    submitted = request.GET.get('submitted') == '1'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect(f'{reverse("contact")}?submitted=1')
    else:
        form = ContactForm()
    return render(request, 'cafe/contact.html', {'form': form, 'submitted': submitted})