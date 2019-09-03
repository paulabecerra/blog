from django.shortcuts import render

#models
from .models import Work

def work_list(request):
    works = Work.objects.all().order_by('-start_date')
    return render(request, 'work/work_positions.html', {'works':works})

# Create your views here.
