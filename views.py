from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from .models import Gujarat_hospital,Appointment,Gujarat_Ngo
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
)
from django.core.mail import EmailMessage
from django.contrib import messages
from django.views.generic.base import TemplateView
import datetime
from django.template import Context
from django.template.loader import render_to_string,get_template


# Create your views here.
def home(request):
    return render(request,'home/home.html')

def gujarat(request):
    context = {
        'gujarat': Gujarat_hospital.objects.all()
    }
    return render(request, 'home/gujarat.html', context)

class GujaratListView(ListView):
    model = Gujarat_hospital
    template_name = 'home/gujarat.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'gujarat'
    paginate_by = 8

class GujaratDetailView(DetailView):
    model = Gujarat_hospital
    template_name = 'home/gujarat_detail.html'

def gujaratNgo(request):
    context = {
        'gujarat_ngo': Gujarat_Ngo.objects.all()
    }
    return render(request, 'home/gujaratNgo.html', context)

class GujaratNgoListView(ListView):
    model = Gujarat_Ngo
    template_name = 'home/gujaratNgo.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'gujarat_ngo'
    paginate_by = 8

class GujaratNgoDetailView(DetailView):
    model = Gujarat_Ngo
    template_name = 'home/gujarat_ngo.html'



def search(request):
    query =request.GET['query']
    
    title_hospitals = Gujarat_hospital.objects.filter(title__icontains = query)
    content_hospitals = Gujarat_hospital.objects.filter(content__icontains = query)
    city_hospitals = Gujarat_hospital.objects.filter(city__icontains = query)
    merge_hospital = title_hospitals.union(content_hospitals)

    hospitals = merge_hospital.union(city_hospitals)

    if len(hospitals)==0:
        messages.warning(request,f'No search results found.Please refine your query')

    context = {'gujarat':hospitals,'query':query}
    return render(request,'home/search.html',context)


class AppointmentTemplateView(TemplateView):
    template_name = 'home/appointment.html'

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("fname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")

        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment, we will email you ASAP!")
        return HttpResponseRedirect(request.path)


class ManageAppointmentTemplateView(ListView):
    template_name = "home/manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3


    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
            "fname":appointment.first_name,
            "date":date,
        }

        message = get_template('home/email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            'kenchowangdi@gmail.com'
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)


    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({   
            "title":"Manage Appointments"
        })
        return context