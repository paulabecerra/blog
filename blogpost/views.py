from django.shortcuts import render

#Post List#
def post_list(request):
    return render(request, 'blogpost/post_list.html', {})
