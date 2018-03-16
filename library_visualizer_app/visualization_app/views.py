from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'visualization_app/index.html', {
        # Insert data here, so template can render it
    })
