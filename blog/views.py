from django.shortcuts import render

# Create your views here.
def hi_view(request):

    return render(request, 'hi.html', {'data': "Hello Django ",})
