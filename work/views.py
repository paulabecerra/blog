from django.shortcuts import render

#models
from .models import Work

def work_list(request):
    works = Work.objects.all()
    return render(request, 'work/work_positions.html', {'works':works})


def work_detail(request):
    work = get_object_or_404(Work, pk=pk)
    return render(request, 'work/work_detail.html')

# Create your views here.
