from .models import Project
from .forms import VisaForm
from .forms import ContactForm
from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail_subject = 'Thanks for Contacting Us!'
            name = form.cleaned_data.get('name')
            message = f"Hi {name}, Thanks for contacting us!"
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'thnks.html')
    else:
        form = ContactForm()

        return render(request, 'contact-us.html', {'form': form})


def visa(request):
    if request.method == 'POST':
        form = VisaForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.save()
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'Name': user.fname + user.lname,
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            # email.content_subtype('html')
            email.send()
            form.save()
            return render(request, 'thanks.html')
        else:
            return render(request, 'visa.html', {'form': form, 'error': 'Form not valid'})
    else:
        form = VisaForm()

        return render(request, 'visa.html', {'form': form})
