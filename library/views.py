from django.shortcuts import render,get_object_or_404, redirect
from library.models import Book, Student, Borrowing, Course, Mentor
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    mentor = Mentor.objects.all().values()
    book = Book.objects.all().values()
    context = {
        'mentor': mentor,
        'book': book,
    }
    return render(request, 'index.html', context)

def databse(request):
    book = Book.objects.all().values()
    borrow = Borrowing.objects.all().values()
    students = Student.objects.all().values()
    context = {
        "book": book,
        "borrow": borrow,
        "students": students,
    }
    return render(request, "databse.html", context)

def course(request):
    course=Course.objects.all().values()
    if request.method=='POST':
        code=request.POST['code']
        description=request.POST['desc']
        data=Course(code=code,description=description)
        data.save()
    dict={
        'data':course
    }
    return render (request,'course.html',dict)

def mentor(request):
    if request.method=='POST':
        cd=request.POST['code']
        name=request.POST['name']
        room=request.POST['room']
        data=Mentor(menid=cd,menname=name,menroomno=room)
        data.save()
        mentors=Mentor.objects.all().values()
        dict={
            'message':'Data saved',
            'mentors':mentors
        }
    else:
        dict={'message':'',
        }
    return render (request,'newmentor.html',dict)

def update_course(request,code):
    data=Course.objects.get(code=code)
    dict={
        'data':data
    }
    return render (request, 'update_course.html', dict)

def save_update_course(request,code):
    description=request.POST['desc']
    data=Course.objects.get(code=code)
    data.desc=description
    data.save()
    return HttpResponseRedirect(reverse('course'))

def delete_course(request,code):
    course=Course.objects.get(code=code)
    if request.method=="POST":
        course.delete()
        return redirect('course')
    
    return render(request,'delete_course.html',{'course':course})   

def search_course(request):
    if request.method=="GET":
        c_code=request.GET.get('c_code')
        if c_code:
            data=Course.objects.filter(code=c_code.upper())
        else:
            data=None
        context={
            'data':data
        }
        return render (request,"search_course.html",context)
    return render(request,'search_course.html')