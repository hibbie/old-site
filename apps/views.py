
import datetime
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template

from hibbie.apps.forms import LlamaContactForm

message_body = """
Name:
{name}

Message: 
{message}

"""


def home(request):
    """
    Homepage for my site.
    """
    return render(request, 'index.html', {
        "timesince": int(datetime.datetime.now().year - 2007)
    })

def about(request):
    """
    Simple about page.
    """
    return render(request, 'about.html')

def contact(request):
    """
    Contact form.
    """
    if request.method == 'POST':
        form = LlamaContactForm(data=request.POST)

        if form.is_valid():
            name = request.POST.get(
                'name'
                , '')
            email = request.POST.get(
                'email'
                , '')
            content = request.POST.get('content', '')
            email = EmailMessage(
                "[hibbie.net] Contact Form",
                message_body.format(name=name,message=content),
                'thomas.hibbard@gmail.com',
                ['thomas.hibbard@gmail.com',],
                headers={'Reply-To': email}
            )
            email.send()
            return redirect('contact')
    else:
        form = LlamaContactForm()

    return render(request, 'contact.html', {
        'form': form,
    },
    )