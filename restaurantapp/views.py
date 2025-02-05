from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .models import Customer
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string
from datetime import datetime
# Create your views here.

def index(request):
    if request.method == 'POST': 
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save customer data
        Customer.objects.create(name=name, email=email, phone=phone, message=message)

        # Prepare email
        subject = 'Thank you for contacting us'
        email_message = render_to_string('restaurantapp/msg.html', {'name': name ,'date':datetime.now})
        from_email = 'rojikc764@gmail.com'
        recipient_list = [email] 

        try:
            email_msg = EmailMessage(subject, email_message, from_email, to=recipient_list)
            email_msg.content_subtype = "html" 
            email_msg.send(fail_silently=True)

            messages.success(request, f"Hi {name}, your form has been successfully submitted. Please check your email for confirmation!")
            return redirect('index')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('index')

    return render(request, 'restaurantapp/index.html')

def about(request):
    return render(request,'restaurantapp/about.html')


def contact(request):
   if request.method == 'POST': 
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save customer data
        Customer.objects.create(name=name, email=email, phone=phone, message=message)

        # Prepare email
        subject = 'Thank you for contacting us'
        email_message = render_to_string('restaurantapp/msg.html', {'name': name ,'date':datetime.now})
        from_email = 'rojikc764@gmail.com'
        recipient_list = [email] 

        try:
            email_msg = EmailMessage(subject, email_message, from_email, to=recipient_list)
            email_msg.content_subtype = "html" 
            email_msg.send(fail_silently=True)

            messages.success(request, f"Hi {name}, your form has been successfully submitted. Please check your email for confirmation!")
            return redirect('contact')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('contact')

   return render(request, 'restaurantapp/contact.html')

def menu(request):
    return render(request,'restaurantapp/menu.html')

def services(request):
    return render(request,'restaurantapp/services.html')


def privacy(request):
    return render(request,'restaurantapp/privacy.html')

def policy(request):
    return render(request,'restaurantapp/policy.html')

def terms(request):
    return render(request,'restaurantapp/terms.html')

def support(request):
    return render(request,'restaurantapp/support.html')

