from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course, Instructor, Contact

def home(request):
    courses = Course.objects.all()[:3]  # Show first 3 courses
    instructors = Instructor.objects.all()[:2]  # Show first 2 instructors
    context = {
        'courses': courses,
        'instructors': instructors,
    }
    return render(request, 'home.html', context)

def courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'courses.html', context)

def about(request):
    instructors = Instructor.objects.all()
    context = {
        'instructors': instructors,
    }
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        messages.success(request, 'Thank you! Your message has been sent successfully.')
        return redirect('contact')
    
    return render(request, 'contact.html')