from django.shortcuts import render, get_object_or_404

#models
from .models import Work

def work_list(request):
    works = Work.objects.all()
    return render(request, 'work/work_positions.html', {'works':works})


def work_detail(request, pk):
    work = get_object_or_404(Work, pk=pk)
    return render(request, 'work/work_detail.html', {'work': work})

# Create your views here.
