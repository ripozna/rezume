from django.urls import path
from .views import register
from .views import write_pdf_view

urlpatterns = [
    path('', register, name='register'), 
    path('write_pdf_view/', write_pdf_view, name='write_pdf_view'),           
] 