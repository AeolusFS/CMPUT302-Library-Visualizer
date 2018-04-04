from django.shortcuts import render, redirect
from django.urls import reverse

from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components

from visualization_app.library_data import lib_info, lib_name

def index(request):
    # pass in each library as an array to the template
    # library data can be made in another py file and imported here
    testing_libraries = [lib_info['testinglibrary'], lib_info['testng'], lib_info['junit4']]
    mock_libraries = [lib_info['mockito']]
    all_libraries = [testing_libraries, mock_libraries]

    return render(request, 'visualization_app/main_page.html', {
        "all_libraries" : all_libraries,
    })

def visualization(request):
    if request.method == 'POST':
        print(request.POST) # The library names should appear in the request dictionary
        # Check with libraries are here, then display them. If empty, well dang, the person submitted an empty form. Display nothing
        
        # Do this for all libraries
        compare_libraries = []
        if 'junit4' in request.POST:
            compare_libraries.append(lib_info['junit4'])
        if 'testinglibrary' in request.POST:
            compare_libraries.append(lib_info['testinglibrary'])
        if 'testng' in request.POST:
            compare_libraries.append(lib_info['testng'])
        if 'mockito' in request.POST:
            compare_libraries.append(lib_info['mockito'])
        # Add more here for more libraries
        
        # List of all the different visualization names
        visualizations = [["Popularity Count"], ["Release Frequency"], ["Last Modified Date"], \
        ["Backwards Compatibility"], ["Stack Overflow"], ["Security & Performance"], ["Issue Data Response Time"], ["Issue Data Resolved Time"]]
        script = []
        div = []


        library_names = []
        library_popularity = []
        for library in compare_libraries:
            library_names.append(library['Name'])
            library_popularity.append(library['Popularity_Count'])
        

        # Popularity Count Graph
        plot = figure(x_range=library_names, plot_height=400, title="Popularity Counts")
        plot.vbar(x=library_names, top=library_popularity, width=0.6)

        plot.xgrid.grid_line_color = None
        plot.y_range.start = 0 

        # Store components - visualizations[0] is Popularity Count
        script, div = components(plot)
        visualizations[0].append(script) # Ensure it is this order
        visualizations[0].append(div)


        # Release Frequency Graph
        x= [1,3,5,7,9,11,13]
        y= [1,2,3,4,5,6,7]
        title = 'y = f(x)'

        plot = figure(title= title , 
            x_axis_label= 'X-Axis', 
            y_axis_label= 'Y-Axis', 
            plot_width =400,
            plot_height =400)

        plot.line(x, y, legend= 'f(x)', line_width = 2)
        # Store components - visualizations[1] is Release Frequency
        script, div = components(plot)
        visualizations[1].append(script)
        visualizations[1].append(div)


        #Feed them to the Django template.
        return render(request, 'visualization_app/visualizations.html', {
            'visualizations' : visualizations,
        })
    
    else:
        return redirect('/') # Go back to main screen

