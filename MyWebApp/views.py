from django.shortcuts import render

def post_list(request):
    return render(request, 'MyWebApp/post_list.html', {})

