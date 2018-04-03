from django.shortcuts import render, redirect
from django.urls import reverse

from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components

from visualization_app.classes import Library
from visualization_app.library_data import lib_info, lib_name

def index(request):
    # pass in each library as an array to the template
    # library data can be made in another py file and imported here
    test_library1 = Library("testinglibrary", "skaefer143", "Testing")
    test_library2 = Library("testng", "cbeust/testng", "Testing")
    test_library3 = Library("mockito", "mockito/mockito", "Mocking")
    testing_libraries = [test_library1, test_library2, lib_info['junit4']]
    mock_libraries = [test_library3]
    all_libraries = [testing_libraries, mock_libraries]

    return render(request, 'visualization_app/main_page.html', {
        "all_libraries" : all_libraries,
    })

def visualization(request):
    if request.method == 'POST':
        print(request.POST) # The library names should appear in the request dictionary
        # Check with libraries are here, then display them. If empty, well dang, the person submitted an empty form. Display nothing

        # List of all the different visualization names
        visualization_names = ["Popularity Count", "Release Frequency", "Last Modified Date", \
        "Backwards Compatibility", "Stack Overflow", "Security & Performance", "Issue Data Response Time", "Issue Data Resolved Time"]


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
        return render(request, 'visualization_app/visualizations.html', {
            'script' : script, 
            'div' : div,
            'visualization_names' : visualization_names,
        })
    
    else:
        return redirect('/') # Go back to main screen

