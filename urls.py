from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.login,name="login"),
    path('admin_template', views.admin_template,name="admin_template"),
    path('student_registration',views.student_registration,name="student_registration"),
    path('student_registration_edit/<int:sid>',views.student_registration_edit,name="student_registration_edit"),
    path('student_registration_delete/<int:sid>',views.student_registration_delete,name="student_registration_delete"),
    path('book_registration',views.book_registration,name="book_registration"),
    path('book_registration_edit/<int:sid>',views.book_registration_edit,name="book_registration_edit"),
    path('book_registration_delete/<int:sid>',views.book_registration_delete,name="book_registration_delete"),
    path('book_registration_view',views.book_registration_view,name="book_registration_view"),
    path('student_book_registration',views.student_book_registration,name="student_book_registration"),
    path('student_book_registration_edit/<int:sid>',views.student_book_registration_edit,name="student_book_registration_edit"),
    path('student_book_registration_delete/<int:sid>',views.student_book_registration_delete,name="student_book_registration_delete"),
    path('student_book_purchase',views.student_book_purchase,name="student_book_purchase"),
    path('student_book_purchase_edit/<int:sid>',views.student_book_purchase_edit,name="student_book_purchase_edit"),
    path('student_book_purchase_delete/<int:sid>',views.student_book_purchase_delete,name="student_book_purchase_delete"),
    path('student_attendance',views.student_attendance,name="student_attendance"),
    path('student_attendance_view',views.student_attendance_view,name="student_attendance_view"),
    path('student_attendance_edit/<int:sid>',views.student_attendance_edit,name="student_attendance_edit"),
    path('student_attendance_delete/<int:sid>',views.student_attendance_delete,name="student_attendance_delete"),
   ]
