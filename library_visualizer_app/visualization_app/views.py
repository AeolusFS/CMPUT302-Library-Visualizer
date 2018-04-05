from django.shortcuts import render, redirect
from django.urls import reverse

import pygal

from visualization_app.library_data import lib_info, lib_name

def index(request):
    # pass in each library as an array to the template
    # library data can be made in another py file and imported here
    testing_libraries = [lib_info['testng'], lib_info['junit4']]
    logging_libraries = [lib_info['slf4j'], lib_info['log4j2'], lib_info['logback'], lib_info['commons logging'], lib_info['tinylog'], lib_info['blitz4j'], lib_info['minlog']]
    utilities_libraries = [lib_info['guava'], lib_info['commons lang']]
    mocking_libraries = [lib_info['mockito'], lib_info['easymock'], lib_info['powermock'], lib_info['jmock']]
    cryptography_libraries = [lib_info['bouncycastle'], lib_info['commons crypto'], lib_info['conceal'], lib_info['chimera'], lib_info['spongycastle'], lib_info['keyczar'], lib_info['conscrypt']]
    json_libraries = [lib_info['gson'], lib_info['json.simple']]
    databases_libraries = [lib_info['h2'], lib_info['derby']]
    security_libraries = [lib_info['shiro'], lib_info['spring security']]
    ormapping_libraries = [lib_info['hibernate orm'], lib_info['mybatis3'], lib_info['ormlite']]
    xml_libraries = [lib_info['xerces2-j'], lib_info['dom4j'], lib_info['jdom']]

    all_libraries = [testing_libraries, logging_libraries, utilities_libraries, mocking_libraries, cryptography_libraries, json_libraries, databases_libraries, security_libraries, ormapping_libraries, xml_libraries]

    return render(request, 'visualization_app/main_page.html', {
        "all_libraries" : all_libraries,
    })

def visualization(request):
    if request.method == 'POST':
        print(request.POST) # The library names should appear in the request dictionary
        # Check with libraries are here, then display them. If empty, well dang, the person submitted an empty form. Display nothing

        # Do this for all libraries
        compare_libraries = []
        #testing_libraries
        if 'junit4' in request.POST:
            compare_libraries.append(lib_info['junit4'])
        if 'testng' in request.POST:
            compare_libraries.append(lib_info['testng'])

        #logging_libraries
        if 'slf4j' in request.POST:
            compare_libraries.append(lib_info['slf4j'])
        if 'log4j2' in request.POST:
            compare_libraries.append(lib_info['log4j2'])
        if 'logback' in request.POST:
            compare_libraries.append(lib_info['logback'])
        if 'commons logging' in request.POST:
            compare_libraries.append(lib_info['commons logging'])
        if 'tinylog' in request.POST:
            compare_libraries.append(lib_info['tinylog'])
        if 'blitz4j' in request.POST:
            compare_libraries.append(lib_info['blitz4j'])
        if 'minlog' in request.POST:
            compare_libraries.append(lib_info['minlog'])

        #utilities_libraries
        if 'guava' in request.POST:
            compare_libraries.append(lib_info['guava'])
        if 'commons lang' in request.POST:
            compare_libraries.append(lib_info['commons lang'])

        #mocking_libraries
        if 'mockito' in request.POST:
            compare_libraries.append(lib_info['mockito'])
        if 'easymock' in request.POST:
            compare_libraries.append(lib_info['easymock'])
        if 'powermock' in request.POST:
            compare_libraries.append(lib_info['powermock'])
        if 'jmock' in request.POST:
            compare_libraries.append(lib_info['jmock'])

        #cryptography_libraries
        if 'bouncycastle' in request.POST:
            compare_libraries.append(lib_info['bouncycastle'])
        if 'commons crypto' in request.POST:
            compare_libraries.append(lib_info['commons crypto'])
        if 'conceal' in request.POST:
            compare_libraries.append(lib_info['conceal'])
        if 'chimera' in request.POST:
            compare_libraries.append(lib_info['chimera'])
        if 'spongycastle' in request.POST:
            compare_libraries.append(lib_info['spongycastle'])
        if 'keyczar' in request.POST:
            compare_libraries.append(lib_info['keyczar'])
        if 'conscrypt' in request.POST:
            compare_libraries.append(lib_info['conscrypt'])

        #json_libraries
        if 'gson' in request.POST:
            compare_libraries.append(lib_info['gson'])
        if 'json.simple' in request.POST:
            compare_libraries.append(lib_info['json.simple'])

        #databases_libraries
        if 'h2' in request.POST:
            compare_libraries.append(lib_info['h2'])
        if 'derby' in request.POST:
            compare_libraries.append(lib_info['derby'])

        #security_libraries
        if 'shiro' in request.POST:
            compare_libraries.append(lib_info['shiro'])
        if 'spring security' in request.POST:
            compare_libraries.append(lib_info['spring security'])

        #ormapping_libraries
        if 'hibernate orm' in request.POST:
            compare_libraries.append(lib_info['hibernate orm'])
        if 'mybatis3' in request.POST:
            compare_libraries.append(lib_info['mybatis3'])
        if 'ormlite' in request.POST:
            compare_libraries.append(lib_info['ormlite'])

        #xml_libraries
        if 'xerces2-j' in request.POST:
            compare_libraries.append(lib_info['xerces2-j'])
        if 'dom4j' in request.POST:
            compare_libraries.append(lib_info['dom4j'])
        if 'jdom' in request.POST:
            compare_libraries.append(lib_info['jdom'])

        # List of all the different visualization names
        visualizations = [["Popularity Count"], ["Release Frequency"], ["Last Modified Date"], \
        ["Backwards Compatibility"], ["Stack Overflow"], ["Security & Performance"], ["Issue Data Response Time"], ["Issue Data Resolved Time"]]
        script = []
        div = []


        library_names = []
        library_popularity = []
        library_QA_SO = []
        for library in compare_libraries:
            library_names.append(library['Name'])
            library_popularity.append(library['Popularity_Count'])
            library_QA_SO.append(library['#_Questions_Asked_SO'])


    # ----- Popularity Count Graph
        bar_chart = pygal.Bar()
        bar_chart.title = 'Repository Popularity Count for Compared Libraries'
        bar_chart.x_labels = library_names
        bar_chart.add('Popularity', library_popularity)
        visualizations[0].append(bar_chart.render_data_uri())
        # with help from http://pygal.org/en/stable/documentation/output.html




    # ----- Release Frequency Graph
    
        

    # ----- Last Modified Date


        # Store components - visualizations[2] is Last Modified Date

    # ----- Backwards Compatibility      


        # Store components - visualizations[3] is Backwards Compatibility

    # ----- Stack Overflow
        bar_chart = pygal.Bar()
        bar_chart.title = 'Number of Questions Asked'
        bar_chart.x_labels = library_names
        bar_chart.add('#_Questions_Asked', library_QA_SO)
        
        # Store components - visualizations[4] is Stack Overflow
        visualizations[4].append(bar_chart.render_data_uri())

    # ----- Security & Performance


        # Store components - visualizations[5] is Security & Performance

    # ----- Issue Data Response Time


        # Store components - visualizations[6] is Issue Data Response Time

    # ----- Issue Data Resolved Time


        # Store components - visualizations[7] is Issue Data Resolved Time

        #Feed them to the Django template.
        return render(request, 'visualization_app/visualizations.html', {
            'visualizations' : visualizations,
        })

    else:
        return redirect('/') # Go back to main screen
