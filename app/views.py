from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *
from django.views.generic import TemplateView,FormView

class Cbv_template(TemplateView):
    template_name='Cbv_template.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #context['name']='yashhari'
        #context['age']=22
        sf= StudentForm()
        context['sf']=sf
        return context

    def post(self,request):
        fd=StudentForm(request.POST)
        if fd.is_valid():
            return HttpResponse(str(fd.cleaned_data))

class Cbv_form(FormView):
    template_name='Cbv_form.html'
    form_class=StudentForm

    def form_valid(self,form):
        return HttpResponse(str(form.cleaned_data))

class Cbv_SchoolForm(FormView):
    template_name='Cbv_SchoolForm.html'
    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('data is inserted')
