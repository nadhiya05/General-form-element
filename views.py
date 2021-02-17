from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .import models
from .models import student_attendance,student,assign_book,purchase_book
from datetime import date
# from django.core.mail import send_mail
# from project1 import settings
from django.contrib import messages



dict={}
# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        if username=="admin":
            if password=="admin":
                obj=student.objects.all()
                return render(request,"admin_template.html",{"obj":obj})
    else:
        return render(request,"index.html")
def admin_template(request):
    obj=student.objects.all()
    return render(request,"admin_template.html",{"obj":obj})

def student_registration(request):
    if request.method=="POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        birthday=request.POST["birthday"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        password=request.POST["password"]
        gender=request.POST["radio1"]
        obj=models.student()
        obj.fname=fname
        obj.lname=lname
        obj.birthday=birthday
        obj.email=email
        obj.phone=phone
        obj.password=password
        obj.gender=gender
        obj.save()
        return redirect('admin_template')
    return render(request,"student_registration.html")

def student_registration_edit(request,sid):
    obj=student.objects.get(id=sid)
    if request.method=="POST":
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        birthday=request.POST["birthday"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        password=request.POST["password"]
        gender=request.POST["radio1"]
        obj=student.objects.get(id=sid)
        obj.fname=fname
        obj.lname=lname
        obj.birthday=birthday
        obj.email=email
        obj.phone=phone
        obj.password=password
        obj.gender=gender
        obj.save()
        return redirect('admin_template')
    return render(request,"student_registration_edit.html",{'obj':obj})

def student_registration_delete(request,sid):
    obj=student.objects.get(id=sid)
    obj.delete()
    return redirect('admin_template')

def book_registration(request):
    if request.method=="POST":
        book_name=request.POST["book_name"]
        book_author=request.POST["book_author"]
        book_price=request.POST["book_price"]
        book_count=request.POST["book_count"]
        myfile = request.FILES.get("book_image")
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        img = fs.url(filename)
        print("imageimageimage", myfile, type(myfile))
        print("imageimageimage",img,type(img))
        obj=models.book()
        obj.namee=book_name
        obj.price=book_price
        obj.count=book_count
        obj.author=book_author
        obj.image=img
        obj.save()
        return redirect('book_registration_view')
    return render(request,"book_registration.html")

def book_registration_edit(request,sid):
    obj=models.book.objects.get(id=sid)
    if request.method=="POST":
        book_name=request.POST["book_name"]
        book_author=request.POST["book_author"]
        book_price=request.POST["book_price"]
        book_count=request.POST["book_count"]
        #image = request.FILES["image"]
        #fs = FileSystemStorage()
        #filename = fs.save(image.name, image)
        #img = fs.url(filename)
        obj=models.book.objects.get(id=sid)
        obj.namee=book_name
        obj.price=book_price
        obj.count=book_count
        obj.author=book_author
        #obj.image=img
        obj.save()
        return redirect('book_registration_view')
    return render(request, "book_registration_edit.html",{'obj':obj})

def book_registration_delete(request,sid):
    obj = models.book.objects.get(id=sid)
    obj.delete()
    return redirect('book_registration_view')


def book_registration_view(request):
    obj = models.book.objects.all()
    return render(request, "book_registration_view.html",{'obj':obj})

def student_book_registration(request):
    obj = models.book.objects.all()
    obj1 = models.student.objects.all()
    obj2 = models.assign_book.objects.all()
    if request.method=="POST":
        name = request.POST["student_name"]
        bname = request.POST["book_name"]

        for x in dict:
            if x == name:
                if dict[x] == bname:
                    messages.success(request,"You cannot same book again")
        student_id = student.objects.get(fname=name)
        st_qry = student.objects.all().filter(fname=name)
        li = list(st_qry)
        for u in li:
            print("jjjjjjjjjjj", u, type(u))
            print("jjjjjjjjj", u.lname)
            print("jjjjjjjjj", u.fname)
            print("jjjjjjjjj", u.class_name)
            print("jjjjjjjjj", u.attendance)
            tot_attenandence = u.attendance + 1
            student_id.attendance = tot_attenandence
            student_id.save()
        for j in st_qry:
            print("eeeeeeeee", j)
        bk_count = models.assign_book.objects.filter(st=student_id.id).count()
        print("oooooooooooo====", bk_count)
        if bk_count >= 2:
            messages.success(request,"You cannot take more than 2 books at a time")
        book_details = models.book.objects.get(namee=bname)
        book_details.count = book_details.count - 1
        book_details.save()
        print("book details count===", book_details.count)
        dict.update({name: bname})
        rdate = request.POST.get('rdate')
        idate = request.POST.get('idate')
        due_date = request.POST["due_date"]
        print(rdate,type(rdate))
        print(idate,type(idate))
        r = rdate.split("-")
        d = due_date.split("-")
        r0 = date(int(r[0]), int(r[1]), int(r[2]))
        d1 = date(int(d[0]), int(d[1]), int(d[2]))
        delta = r0 - d1
        print(delta.days)
        if delta.days > 0:
            finee = delta.days * 1
            print("finnnnnnnnnn", finee)
        obj = models.assign_book()
        obj.st = models.student.objects.get(fname=name)
        obj.bt = models.book.objects.get(namee=bname)
        obj.rdate = rdate
        obj.idate = idate
        obj.fine = finee
        obj.due_date = due_date
        obj.save()
        st_id = models.student.objects.get(fname=name)
        st_id.save()
        return redirect('student_book_registration')
    return render(request,'student_book_registration.html',{'student_objects':obj1,'book_objects':obj,'student_book_objects':obj2})

def student_book_registration_edit(request,sid):
    obj = models.book.objects.all()
    obj1 = models.student.objects.all()
    assign_books_objects_id = models.assign_book.objects.get(id=sid)
    print("ppppppppppppppppppp", assign_books_objects_id.id)
    student_objects = models.student.objects.all()
    book_objects = models.book.objects.all()
    if request.method == "POST":
        name = request.POST["student_name"]
        bname = request.POST["book_name"]
        rdate = request.POST.get('rdate')
        idate = request.POST.get('idate')
        due_date = request.POST.get('due_date')
        obj = models.assign_book.objects.get(id=sid)
        obj.st = models.student.objects.get(id=name)
        obj.bt = models.book.objects.get(id=bname)
        r = rdate.split("-")
        d = due_date.split("-")
        r0 = date(int(r[0]), int(r[1]), int(r[2]))
        d1 = date(int(d[0]), int(d[1]), int(d[2]))
        delta = r0 - d1
        print(delta.days)
        if delta.days > 0:
            finee = delta.days * 1
            print("finnnnnnnnnn", finee)
            obj.fine = finee
        obj.rdate = rdate
        obj.idate = idate
        obj.save()
        return redirect('student_book_registration')
    return render(request,"student_book_register_edit.html",
                  {'obj':assign_books_objects_id,'student_objects':obj1,
                                                             'book_objects':obj})

def student_book_registration_delete(request,sid):
    obj=assign_book.objects.get(id=sid)
    obj.delete()
    return redirect('student_book_registration')

def student_book_purchase(request):
    student_objects=models.student.objects.all()
    book_objects=models.book.objects.all()
    purchase_obj = purchase_book.objects.all()
    if request.method=="POST":
        name=request.POST["student_name"]
        bname=request.POST["book_name"]
        purchase_date=request.POST["idate"]
        obj=models.purchase_book()
        obj.st=models.student.objects.get(fname=name)
        obj.bt=models.book.objects.get(namee=bname)
        for e in models.book.objects.all().filter(namee=bname):
            print("ooooooo",e.price)
        for q in models.book.objects.all().filter(namee=bname):
            print("kkkkkkkk",q.count)
        q.count=q.count-1
        print("quanttttttt",q.count)
        obj.stock_left=q.count
        obj.price=e.price
        obj.purchase_date=purchase_date
        obj.save()
        return redirect('student_book_purchase')
    return render(request,'student_book_purchase.html',{"student":student_objects,"book":book_objects,"purchase_obj":purchase_obj})

def student_book_purchase_edit(request,sid):
    student_objects=models.student.objects.all()
    book_objects=models.book.objects.all()
    purchase_obj = purchase_book.objects.get(id=sid)
    if request.method=="POST":
        name=request.POST["student_name"]
        bname=request.POST["book_name"]
        purchase_date=request.POST["purchase_date"]
        price=request.POST["price"]
        obj=models.purchase_book.objects.get(id=sid)
        obj.st=models.student.objects.get(fname=name)
        obj.bt=models.book.objects.get(namee=bname)
        for e in models.book.objects.all().filter(namee=bname):
            print("ooooooo",e.price)
        for q in models.book.objects.all().filter(namee=bname):
            print("kkkkkkkk",q.count)
        q.count=q.count-1
        print("quanttttttt",q.count)
        obj.stock_left=q.count
        obj.price=price
        obj.purchase_date=purchase_date
        obj.save()
        return redirect('student_book_purchase')
    return render(request,'student_book_purchase_edit.html',{"student":student_objects,"book":book_objects,"purchase_obj":purchase_obj})

def student_book_purchase_delete(request,sid):
    purchase_obj = purchase_book.objects.get(id=sid)
    purchase_obj.delete()
    student_objects = models.student.objects.all()
    book_objects = models.book.objects.all()
    purchase_obj = purchase_book.objects.all()
    return render(request, 'student_book_purchase.html',
                  {"students": student_objects, "book": book_objects, "purchase_obj": purchase_obj})

def student_attendance(request):
    print("Successfully Entered in StudentAttendance")
    student_objects=student.objects.all()
    if request.method=="POST":
        st_id=request.POST["student_id"]
        obj=models.student_attendance()
        obj.st=models.student.objects.get(id=st_id)
        obj.date="2020-07-07"
        present=request.POST["present"]
        absent=request.POST["absent"]
        print("ppppppppppppppppppp",present,absent)
        obj.save()
        pp = models.student_attendance.objects.all()
        return render(request, "student_attendance_view.html", {"obj": pp})
    return render(request,"student_attendance.html",{"student_objects":student_objects})

def student_attendance_view(request):
    pp = models.student_attendance.objects.all()
    return render(request, "student_attendance_view.html", {"obj": pp})


def student_attendance_edit(request,sid):
    obj=student_attendance.objects.get(id=sid)
    if request.method=="POST":
        st_id=request.POST["student_id"]
        attendance=request.POST["attendance"]
        obj=models.student_attendance()
        obj.st=models.student.objects.get(id=st_id)
        obj.date="2020-07-07"
        if attendance=="absent":
            obj.attendance="absent"
        else:
            obj.attendance="present"
        obj.save()
        pp = models.student_attendance.objects.all()
        return render(request, "student_attendance_view.html", {"obj": pp})
    return render(request,"student_attendence_edit.html",{"obj":obj})



def student_attendance_delete(request,sid):
    obj=student_attendance.objects.get(id=sid)
    obj.delete()
    return redirect('student_attendance_view')
