from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'belt_exam_2_app/page.html')
