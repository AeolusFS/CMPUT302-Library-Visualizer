from django.shortcuts import render, redirect
from django.http import HttpResponse

from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components

from visualization_app.classes import Library

def index(request):
    # pass in each library as an array to the template
    # library data can be made in another py file and imported here
    test_library1 = Library("junit4", "junit-team/junit4", "testing")
    test_library2 = Library("testng", "cbeust/testng", "testing")
    libraries = [test_library1, test_library2]

    return render(request, 'visualization_app/main_page.html', {
        "libraries" : libraries,
    })

def test(request):
    x= [1,3,5,7,9,11,13]
    y= [1,2,3,4,5,6,7]
    title = 'y = f(x)'

    plot = figure(title= title , 
        x_axis_label= 'X-Axis', 
        y_axis_label= 'Y-Axis', 
        plot_width =400,
        plot_height =400)

    plot.line(x, y, legend= 'f(x)', line_width = 2)
    #Store components 
    script, div = components(plot)

    #Feed them to the Django template.
    return render(request, 'visualization_app/test.html', {
        'script' : script , 
        'div' : div
    })

