from django.contrib import admin
from .models import student,book,assign_book,purchase_book,student_attendance

# Register your models here.
admin.site.register(student)
admin.site.register(book)
admin.site.register(assign_book)
admin.site.register(purchase_book)
admin.site.register(student_attendance)
