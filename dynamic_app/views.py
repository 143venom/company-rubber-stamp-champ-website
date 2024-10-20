from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from .models import *
from service_page.models import Service
from blog_app.models import Post
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages, auth
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


# Create your views here.
def indesx(request):
    sliders = Slider.objects.all().order_by("-pub_date")[:4]
    services = Service.objects.all()
    testimonial = Testimonial.objects.all()

    if request.method == "POST":
        # Retrieve form data from POST request
        name = request.POST.get("name")
        email = request.POST.get("email")
        service = request.POST.get("service")
        message = request.POST.get("message")

        if name and email and service and message:

            Quote.objects.create(
                name=name, emial=email, service=service, message=message
            )

            subject = "New Quote Request"
            message_body = (
                f"Name: {name}\nEmail: {email}\nService: {service}\nMessage: {message}"
            )
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ["14ing.dev@gmail.com"]

            send_mail(subject, message_body, from_email, recipient_list)

    return render(request,"index.html",{"services": services, "sliders": sliders, "testimonials": testimonial},)


def aboutUs(request):
    return render(request, "about.html")


# def blog(request):
#     return render(request, "blog.html")


# def stamps(request):
#     return render(request, "service.html")


def contact(request):
    if request.method == "POST":
        # Retrieve form data from POST request
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        if name and email and subject and message:

            # subject = "The contact form"
            message_body = (
                f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
            )
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ["14ing.dev@gmail.com"]

            send_mail(subject, message_body, from_email, recipient_list)

    return render(request, "contact.html")


def printingServices(request):
    ps = PrintingServices.objects.all().order_by("-id")
    context = {"ps": ps}
    return render(request, "printing.html", context)


def itServices(request):
    message = None
    service = ItServices.objects.all().order_by("-id")
    context = {"services": service,
                "message": message}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        website = request.POST.get("website")
        comment = request.POST.get("comment")
        if name and email and website and comment:
            GetItServices.objects.create(name=name, email=email, website=website, comment=comment)
            message = messages.success(request, "Thank you for your comment!")
            return redirect("itservice")
        else:
            message = messages.error(request, 'Please fill in all fields.')
    
    return render(request, "itservice.html", context)


def photographyServices(request):
    message = None
    photographyservice = PhotographyServices.objects.all().order_by("-id")
    context = {"photographyservices": photographyservice,
                "message": message}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        comment = request.POST.get("comment")
        if name and email and mobile and comment:
            GetPhotographyServices.objects.create(name=name, email=email, phone_number=mobile, comment=comment)
            message = messages.success(request, "Thank you for your comment!")
            return redirect("photographyservice")
        else:
            message = messages.error(request, 'Please fill in all fields.')
    
    return render(request, "photographyservice.html", context)


def search(request):
    query = request.GET["query"]
    if len(query) > 80:
        posts = []
    else:
        posts = Post.objects.filter(title__icontains=query)
    context = {"posts": posts, "query": query}
    return render(request, "search.html", context)


# @login_required
# def indexPage(request):
#     sliders = Slider.objects.all().order_by("-pub_date")[:4]
#     return render(request, 'index.html', {'sliders':sliders})

# def createSuperuser(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         full_name = request.POST['full_name']
#         address = request.POST['address']
#         phone_number = request.POST['phone_number']
#         password = request.POST['password']
#         password_repeat = request.POST['password_repeat']

#         if password == password_repeat:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email already exists')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_superuser(email=email, full_name=full_name, address=address, phone_number=phone_number, password=password)
#                 user.save()
#                 login(request, user)
#                 return redirect('index-page')
#         else:
#             message = messages.info(request, 'Passwords do not match')
#             return redirect('create-superuser')
#     else:
#         return render(request, "register_superuser.html", {'message': message})

# def loginPage(request):
#     message = None
#     if request.user.is_authenticated:
#         return redirect('index-page')
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['psw']
#         user = auth.authenticate(request,email=email,password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index-page')
#         else:
#             message = messages.info(request, 'Invalid credentials')
#             return redirect('login-page')
#     else:
#         return render(request, 'login.html', {'message': message})

# def logout(request):
#     auth.logout(request)
#     return redirect('login-page')
