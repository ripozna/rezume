from django.shortcuts import render
from rezume.forms import  RegistrationForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def register(request):
    form = RegistrationForm(request.POST,request.FILES or None)
    message = 'Fill the blank'
    print(form)
    if request.method =='POST' and form.is_valid():
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

        buffer = BytesIO()
        p = canvas.Canvas(buffer)

        # Start writing the PDF here

        p.drawString(10, 800, 'name:' + request.POST.get('name'))
        p.drawString(10, 750, 'surname:' + request.POST.get('surname'))
        p.drawString(10, 700, 'phone_number:' + request.POST.get('phone_number'))
        p.drawString(10, 650, 'date_of_birth:' + request.POST.get('date_of_birth'))
        p.drawString(10, 600, 'purpose :' + request.POST.get('purpose'))
        p.drawString(10, 550, 'education:' + request.POST.get('education'))
        p.drawString(10, 500, 'professional_skills:' + request.POST.get('professional_skills'))
        p.drawString(10, 450, 'personal_qualities:' + request.POST.get('personal_qualities'))
        p.drawString(10, 400, 'additional_information:' + request.POST.get('additional_information'))
        # End writing

        p.showPage()
        p.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)

        return response
    return render(request, 'rezume.html', {'form': form, 'message':message})
    

def write_pdf_view(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Start writing the PDF here

    p.drawString(10, 800, 'name:')
    p.drawString(10, 750, 'surname:')
    p.drawString(10, 700, 'phone_number:')
    p.drawString(10, 650, 'date_of_birth:')
    p.drawString(10, 550, 'purpose :')
    p.drawString(10, 500, 'education:')
    p.drawString(10, 450, 'professional_skills:')
    p.drawString(10, 400, 'personal_qualities:')
    p.drawString(10, 350, 'additional_information:')
    # End writing

    p.showPage()
    p.save()
    # date_of_birth = models.CharField(max_length=20 )
    
    
    
    
    
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
# Create your views here.
