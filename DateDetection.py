'''
1)tell user to input date in for DD/MM/YYYY
2)check if date entered passes regex checks
  daymtch = re.compile(r'((31)|(2[0-9])|(1[1-9])|(0[1-9]))')
  monmtch = re.compile(r'((0[1-9])|(1[1|2]))')
  yearmtch = re.compile(r'(1|2)[0-9]{3}')

3)if match fails inform user to quit or re-enter data(have infinite loop or quit)

4)if correct date continue

datechk = re.compile(r'(((31)|(2[0-9])|(1[1-9])|(0[1-9]))/((0[1-9])|(1[1|2]))/([12][0-9]{3}))')
mo = datechk.search('31/04/2021')

5)access the day, month and year from tuple in list returned from datechk regex object


5)determine if date a legitmate calendar date

'''
import re, datetime, sys

isInLoop = False
# outer datedetection loop
while True:
    # inner loop set check date
    while True:
        if isInLoop != True:
            print('Enter date to check in format of dd/mm/yyyy(max year: 2999)\nOR type "q" to quit ')
            isInLoop = True
        else:
            print('Enter another date to check in format of dd/mm/yyyy(max year: 2999)\nOR type "q" to quit ')
        date = input()
        if date == "q":
            sys.exit() # Quit the program
        else:
            datechk = re.compile(r'(((31)|(2[0-9])|(1[1-9])|(0[1-9]))/((0[1-9])|(1[1|2]))/([12][0-9]{3}))')
            mo = datechk.search(date)
            if mo == None:
                print()
                print('Incorrect formatting for date!')
                day, month, year = date.split('/')
                corrections = []
                daymtch = re.compile(r'((31)|(2[0-9])|(1[1-9])|(0[1-9]))')
                moday = daymtch.search(day)
                monmtch = re.compile(r'((0[1-9])|(1[1|2]))')
                momonth = monmtch.search(month)
                yearmtch = re.compile(r'(1|2)[0-9]{3}')
                moyear = yearmtch.search(year)
                if (moday == None):
                    corrections.append('day')
                if momonth == None:
                    corrections.append('month')
                if moyear == None:
                    corrections.append('year')
                
                for i in corrections:
                    print(i, end=', ')
                print('value(s) are incorrect')
                
                print('Please re-enter date!')
                isInLoop  = False
                print()
                break
            else:
                day = mo[2]
                month = mo[7]
                year = mo[10]
                print()
                isValidDate = True
                try :
                    datetime.datetime(int(year),int(month),int(day))
                except ValueError :
                    isValidDate = False

                if(isValidDate) :
                    print ("Input date is valid ..")
                    print()
                else :
                    print ("Input date is not valid..")
                    print()
                break
