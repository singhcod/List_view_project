from django.shortcuts import render
from .models import Student

# Create your views here.
from django.views.generic import ListView,DetailView


class StidentListView(ListView):
    model = Student   #default
    template_name = 'list_app/student.html'
    context_object_name = 'student'

    #
    # def get_queryset(self):
    #     return Student.objects.filter(address='noida')
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args,**kwargs)
    #     context['fresher'] = Student.objects.all().order_by('name')
    #     return context


    #for set dynamic templete set

    # def get_template_names(self):
    #     if self.request.COOKIES['user'] == 'singh':
    #         templete_name = 'list_app/singh.html'
    #     else:
    #         templete_name = self.templete_name
    #     return [templete_name]


class StudentDetailView(DetailView):
    model = Student
    template_name = 'list_app/detail.html'
    context_object_name = 'student'

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['all_student'] = self.model.objects.all().order_by('name')
        return context


