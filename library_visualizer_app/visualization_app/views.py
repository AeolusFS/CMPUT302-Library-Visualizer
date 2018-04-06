from django.shortcuts import render, redirect
from django.urls import reverse

import pygal
from pygal.style import Style

from visualization_app.library_data import lib_info, lib_name

from datetime import date, datetime, timedelta
from dateutil import relativedelta

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
        # print(request.POST) # The library names should appear in the request dictionary
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

        # set up library arrays
        library_names = []
        library_popularity = []
        library_releasedates = []
        library_lastModifiedDate = []
        library_breakingChanges = []
        library_QA_SO = []
        library_lastDiscussedSO = []
        library_Secruity_Performance = []
        library_responsetime = []
        library_resolvedtime = []


        for library in compare_libraries:
            library_names.append(library['Name'])
            library_popularity.append(library['Popularity_Count'])
            releaseDates = []
            for releaseDate in library['Release_Dates']:
                datefilter = datetime.today() - timedelta(days=365)
                if datetime.strptime(releaseDate, "%Y-%m-%d") > datefilter:
                    releaseDates.append(datetime.strptime(releaseDate, "%Y-%m-%d"))
            library_releasedates.append(releaseDates)
            library_lastModifiedDate.append(datetime.strptime(library['Last_Modification_Date'], "%Y-%m-%d"))
            library_breakingChanges.append(library['#_Breaking_Changes'])
            library_QA_SO.append(library['#_Questions_Asked_SO'])
            try:
                library_lastDiscussedSO.append(datetime.strptime(library['Last_Discussed_SO'], "%Y-%m-%d"))
            except: # No date
                library_lastDiscussedSO.append(None)

            init_count = [0, 0, 0, 0] # Peformance - Sercuity - Both - Neither
            for issue_ID in library['Issue_Data']:
                if library['Issue_Data'][issue_ID]['Performance_Issue'] == 'Yes':
                    if library['Issue_Data'][issue_ID]['Security_Issue'] == 'Yes':
                        init_count[2] += 1
                    else:
                        init_count[0] += 1
                else:
                    if library['Issue_Data'][issue_ID]['Security_Issue'] == 'Yes':
                        init_count[1] += 1
                    else:
                        init_count[3] += 1
            library_Secruity_Performance.append(init_count)

            timecategories = [0, 0, 0, 0, 0] #[<day, <week, <month, >month, still pending]
            for issue_id in library['Issue_Data']:
                skipflag = False
                creationdate = datetime.strptime(library['Issue_Data'][issue_id]['Issue_Creation_Date'], "%Y-%m-%d %H:%M:%S")
                try:
                    closedate = datetime.strptime(library['Issue_Data'][issue_id]['Issue_Close_Date'], "%Y-%m-%d %H:%M:%S")
                except: #date is none meaning issue is pending
                    timecategories[4] += 1
                    #print('pending')
                    skipflag = True

                if skipflag == False:
                    #hours difference https://stackoverflow.com/questions/5612129/converting-date-into-hours
                    resolvetime = (closedate - creationdate).total_seconds()/3600.0
                    #print(resolvetime, creationdate, closedate, issue_id)

                    if resolvetime < 24: # less than one day
                        timecategories[0] += 1
                    elif resolvetime < 168: #less than one week
                        timecategories[1] += 1
                    elif resolvetime < 720: #less than one month (30 days)
                        timecategories[2] += 1
                    elif resolvetime >= 720: #greater than or equal to a month (30 days)
                        timecategories[3] += 1
            #print(timecategories)
            library_resolvedtime.append(timecategories)

            timecategories1 = [0, 0, 0, 0, 0] #[<day, <week, <month, >month, no response]
            for issue_id in library['Issue_Data']:
                skipflag1 = False
                creationdate = datetime.strptime(library['Issue_Data'][issue_id]['Issue_Creation_Date'], "%Y-%m-%d %H:%M:%S")
                try:
                    responsedate = datetime.strptime(library['Issue_Data'][issue_id]['Date_of_First_Comment'], "%Y-%m-%d %H:%M:%S")
                except: #date is none meaning no comment
                    timecategories1[4] += 1
                    #print('pending')
                    skipflag1 = True

                if skipflag1 == False:
                    #hours difference https://stackoverflow.com/questions/5612129/converting-date-into-hours
                    resolvetime = (responsedate - creationdate).total_seconds()/3600.0
                    #print(resolvetime, creationdate, closedate, issue_id)

                    if resolvetime < 24: # less than one day
                        timecategories1[0] += 1
                    elif resolvetime < 168: #less than one week
                        timecategories1[1] += 1
                    elif resolvetime < 720: #less than one month (30 days)
                        timecategories1[2] += 1
                    elif resolvetime >= 720: #greater than or equal to a month (30 days)
                        timecategories1[3] += 1
            #print(timecategories)
            library_responsetime.append(timecategories1)



















    #--------- CUSTOM STYLE, USE THIS -----------------#
        custom_style = Style(
            label_font_size = 25,
            major_label_font_size = 25,
            value_font_size = 25,
            value_label_font_size = 25,
            title_font_size = 25,
            legend_font_size = 25,
            tooltip_font_size = 15)
        log_style = Style(
            label_font_size = 12,
            major_label_font_size = 12,
            value_font_size = 25,
            value_label_font_size = 25,
            title_font_size = 25,
            legend_font_size = 25,
            tooltip_font_size = 15)


    # ----- Popularity Count Graph
        bar_chart = pygal.Bar(
            dynamic_print_values=True,
            style=log_style,
            legend_at_bottom=True,
            logarithmic=True)
        bar_chart.title = 'Repository Popularity Count for Compared Libraries'
        #bar_chart.x_labels = library_names
        for libraries in range(len(library_popularity)):
            bar_chart.add(library_names[libraries], library_popularity[libraries])
        visualizations[0].append(bar_chart.render_data_uri())
        # with help from http://pygal.org/en/stable/documentation/output.html


    #ATTEMPT TO MAKE A FILTER
        #today = date.today()
        #https://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
        #date_list = [today - timedelta(days=x) for x in range(0, 365)]
        #dateline.x_labels = date_list
    # ----- Release Frequency Graph
        dateline = pygal.DateLine(
            show_y_labels=False,
            x_label_rotation=25,
            style=custom_style,
            height=500,
            legend_at_bottom=True,
            show_x_guides=True)
        dateline.title = "Release Frequency Graph"
        maxYAxis = 0.9
        for libraryIndex in range(len(library_releasedates)):
            releaseDatesTuple = []
            for releaseDatesIndex in range(len(library_releasedates[libraryIndex])):
                releaseDatesTuple.append((library_releasedates[libraryIndex][releaseDatesIndex], maxYAxis))
            maxYAxis -= 0.1
            dateline.add(library_names[libraryIndex], releaseDatesTuple, dots_size=15)
        visualizations[1].append(dateline.render_data_uri())


    # ----- Last Modified Date
        # Make x_labels, one month before min and one month after max
        firstDisplayedDate = getMonthDelta(min(library_lastModifiedDate), -1) # Get a month before min date
        lastDisplayedDate = getMonthDelta(max(library_lastModifiedDate), 1) # Get a month after
        allMonths = monthsInBetween(firstDisplayedDate, lastDisplayedDate)
        dateline = pygal.DateLine(
            dynamic_print_values=True,
            x_label_rotation=20,
            show_y_labels=False,
            legend_at_bottom=True,
            style=custom_style,
            height=500,
            show_x_guides=True)
        # ALSO DON'T NEED - just pollutes the x - axis
        # dateline.x_labels = allMonths
        dateline.title = 'Repository Last Modified Date'
        maxYAxis = 0.9
        for index in range(len(library_lastModifiedDate)):
            dateline.add(library_names[index], [(library_lastModifiedDate[index], maxYAxis)], dots_size=25)
            maxYAxis -= 0.1
        visualizations[2].append(dateline.render_data_uri())
        # Store components - visualizations[2] is Last Modified Date

    # ----- Backwards Compatibility
        # make the x-axis labels pretty
        # allDates = []
        # for library_datelist in library_releasedates:
        #     allDates += library_datelist

        bar_chart = pygal.DateLine(
            style=log_style,
            x_label_rotation=25,
            legend_at_bottom=True,
            show_x_guides=True,
            logarithmic=True)
        bar_chart.title = 'Number of Breaking Changes'
        # DON'T NEED - bar_chart.x_labels = map(lambda d: d.strftime('%Y-%m-%d'), allDates)
        for libraryIndex in range(len(library_breakingChanges)):
            release_breakingChange_tuples = []
            #print(str(len(library_releasedates[libraryIndex])) + " - " + str(len(library_breakingChanges[libraryIndex])))
            for dateIndex in range(min(len(library_releasedates[libraryIndex]), len(library_breakingChanges[libraryIndex]))):
                # So, breaking changes and released dates aren't exactly the same. That's why we look for min(), so things dont break
                release_breakingChange_tuples.append((library_releasedates[libraryIndex][dateIndex], library_breakingChanges[libraryIndex][dateIndex]))
            bar_chart.add(library_names[libraryIndex], release_breakingChange_tuples, dots_size=5)

        visualizations[3].append(bar_chart.render_data_uri())
        # Store components - visualizations[3] is Backwards Compatibility

    # ----- Stack Overflow
        bar_chart = pygal.Bar(
            dynamic_print_values=True,
            style=log_style,
            logarithmic=True)
        bar_chart.title = 'Number of Questions Asked'
        #bar_chart.x_labels = library_names
        for libraries in range(len(library_QA_SO)):
            bar_chart.add(library_names[libraries], library_QA_SO[libraries])

        visualizations[4].append(bar_chart.render_data_uri())
        # Store components - visualizations[4] is Stack Overflow

        # Second chart
        dateline = pygal.DateLine(
            dynamic_print_values=True,
            x_label_rotation=20,
            show_y_labels=False,
            legend_at_bottom=True,
            style=custom_style,
            height=400,
            show_x_guides=True)
        dateline.title = 'Last Discussed on Stack Overflow'

        notDiscussed = []
        for index in range(len(library_lastDiscussedSO)):
            dateline.add(library_names[index], [(library_lastDiscussedSO[index], 0.5)], dots_size=25)
            if library_lastDiscussedSO[index] == None:
                notDiscussed.append(library_names[index])

        visualizations[4].append(dateline.render_data_uri())
        # Store components - visualizations[4] is Stack Overflow


    # ----- Security & Performance
        labels = ['Performance','Security','Both','Neither']
        tran_data = [[],[],[],[]]
        bar_chart = pygal.StackedBar(
            dynamic_print_values=True,
            style=log_style,
            legend_at_bottom=True,
            logarithmic=True)
        bar_chart.title = 'Security and Performance Percentage'
        bar_chart.x_labels = library_names

        for libraries in range(len(library_Secruity_Performance)):
            for label_num in range(len(labels)):
                tran_data[label_num].append(library_Secruity_Performance[libraries][label_num])
        for label in range(len(labels)):
            bar_chart.add(labels[label], tran_data[label])

        # Store components - visualizations[5] is Security & Performance
        visualizations[5].append(bar_chart.render_data_uri())

    # ----- Issue Data Response Time

        labels = ['<Day','<Week','<Month','>Month', 'No response']
        bar_chart = pygal.Bar(dynamic_print_values=True,
            legend_at_bottom=True
            )
        bar_chart.title = 'Issue Data Response Time'
        bar_chart.x_labels = labels
        for libraries in range(len(library_responsetime)):
            bar_chart.add(library_names[libraries], library_responsetime[libraries])
        visualizations[6].append(bar_chart.render_data_uri())



        # Store components - visualizations[6] is Issue Data Response Time

    # ----- Issue Data Resolved Time
        labels = ['<Day','<Week','<Month','>Month', 'Pending']
        bar_chart = pygal.Bar(dynamic_print_values=True,
            legend_at_bottom=True
            )
        bar_chart.title = 'Issue Data Resolved Time'
        bar_chart.x_labels = labels
        for libraries in range(len(library_resolvedtime)):
            bar_chart.add(library_names[libraries], library_resolvedtime[libraries])
        visualizations[7].append(bar_chart.render_data_uri())


        # Store components - visualizations[7] is Issue Data Resolved Time

        #Feed them to the Django template.
        return render(request, 'visualization_app/visualizations.html', {
            'visualizations' : visualizations,
            'notDiscussed' : notDiscussed,
        })

    else:
        return redirect('/') # Go back to main screen

def getMonthDelta(inputDate, delta):
    first_day = inputDate.replace(day=1)
    return first_day + relativedelta.relativedelta(months=+delta)

def monthsInBetween(firstDate, lastDate):
    # With help from https://dateutil.readthedocs.io/en/stable/relativedelta.html
    sameMonth = False
    iteratorDate = firstDate
    dateList = []
    while sameMonth == False:
        if iteratorDate.month == lastDate.month and iteratorDate.year == lastDate.year:
            sameMonth = True # I guess don't really need this
            break
        dateList.append(iteratorDate)
        iteratorDate = iteratorDate + relativedelta.relativedelta(months=+1)
    dateList.append(iteratorDate)
    return dateList
