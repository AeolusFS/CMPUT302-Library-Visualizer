# This file will store python variables, or something, full of the data we want to display
lib_name = ['junit4', 'testng', 'slf4j', 'log4j2', 'logback', 'commons logging', 'tinylog', 'blitz4j', 'minlog', 'guava', 'commons lang', 'mockito', 'easymock', 'powermock', 'jmock', 'bouncycastle', 'commons crypto', 'conceal', 'chimera', 'spongycastle', 'keyczar', 'conscrypt', 'gson', 'json simple', 'h2', 'derby', 'shiro', 'spring security', 'hibernate orm', 'mybatis3', 'ormlite', 'xerces2-j', 'dom4j', 'jdom']

# lib_info format
#    ' ':{
#        'Git_Rep': ,                                      
#        'Domain': ,                                       
#        'Popularity_Count': ,                   
#        'Last_Modification_Date':                         
#        'Last_Discussed_SO':' ',
#        '#_Questions_Asked_SO': ,
#        'Release_Dates':[],
#        '#_Breaking_Changes':[],
#        'issue_data':{
#            1:{                                         
#               'Issue_Creation_Date':' ',
#               'Issue_Close_Date':' ',
#               'Date_of_First_Comment': ,
#               'Performance_Issue': ,
#               'Security_Issue':
#            }
#            ...
#        }
#    }

# EX. junit4 github repository
# lib_info[junit4][Git_Rep] = junit-team/junit4
# lib_info[junit4][issue_data][1][Performance_Issue] = False

lib_info = {
    'junit4':{
        'Git_Rep':'junit-team/junit4',
        'Domain':'testing',
        'Popularity_Count':56201,
        'Last_Modification_Date':'2018-02-15',
        'Last_Discussed_SO':'2018-02-20',
        '#_Questions_Asked_SO':17789,
        'Release_Dates':['2004-12-28', '2009-04-14', '2009-07-28', '2009-10-27', '2009-10-27', '2009-11-17', '2009-12-01', '2009-12-08', '2010-04-08', '2011-01-03', '2011-07-06', '2011-08-12', '2011-08-22', '2011-09-29', '2012-10-15', '2012-11-13', '2014-07-27', '2014-09-25', '2014-11-09', '2014-12-04'],
        '#_Breaking_Changes':[0, 88, 56, 0, 44, 65, 10, 4, 387, 41, 0, 0, 3, 7, 0, 0, 23, 20, 2, 1],
        'issue_data':{
            1:{
                'Issue_Creation_Date':'2009-05-22 13:26:30',
                'Issue_Close_Date':'2009-06-04 4:16:29',
                'Date_of_First_Comment':None,
                'Performance_Issue':False,
                'Security_Issue':False
            },
            2:{}
        }
    }
}