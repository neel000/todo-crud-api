
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import StudentList
# Create your views here.
from . forms import StudentListForm

def template_path(page):
    return f"pages/{page}"


class HomeView(View):
    def get(self, request):
        stu = StudentList.objects.all()
        form = StudentListForm()
        show = {'student':stu, 'form':form}
        return render(request, template_path('home_index.html'), show)
    
    def post(self, request):
        form = StudentListForm(request.POST)
        show = {'form':form}
        if not form.is_valid():
            return render(request, template_path('home_index.html'), show)
        
        form.save()    
        return redirect('/')

class StudentView(View):
    def get(self, request, id):
        form = StudentListForm(instance=StudentList.objects.get(id=int(id)))
        show = {'form':form, 'id':id}
        return render(request, template_path('student_view.html'), show)
    
    def post(self, request, id):
        stu = StudentList.objects.get(id=int(id))
        form = StudentListForm(request.POST, instance=stu)
        show = {'form':form, 'id':id}
        tag = request.POST.get('tag', None)
        if not tag:
            if not form.is_valid():
                return render(request, template_path('student_view.html'), show)
            form.save()    
        
        # elif tag == 'delete':
        #     stu.delete()
            
            
        
        
        
        
        return redirect(f'/{id}')    
    
    