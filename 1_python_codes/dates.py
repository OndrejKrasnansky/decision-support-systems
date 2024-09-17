import xml.etree.ElementTree as ET
import csv
import datetime



def parse_dates_xml(input_file):
# Parse the XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    date_list = []
    date_pk = [] 
    for i in root.iter():
        if i.tag == 'date':
            date_list.append(i.text) # store dates from xml file
        elif i.tag == 'date_pk':
            date_pk.append(i.text) # store date_pk from xml file
    return date_list,date_pk







def get_date_csv(output_file):
    date_splitted =[]
    date_list,date_pk =parse_dates_xml('C:\\Users\\ondre\\Documents\\UNIPI updated\\UNIPI\\Second Year\\Laboratory for DS\\LDS_Project_2023\\dates.xml')

    with open(output_file, 'w', newline='') as csvdate:  # open new csv file where it will be created the dataset 
        writer = csv.writer(csvdate) # read as reader (using lists)
        writer.writerow(['date_id','date','year','month','day','day_of_the_week','quarter'])  # write the header
        
        for i in range(len(date_list)): # iterate through indexes of date_lists where I have stored all of my lists
            date_datetime = datetime.datetime.strptime(date_list[i], '%Y-%m-%d %H:%M:%S').date()  #.date() to don't have time
            day_of_the_week = date_datetime.strftime('%A')
            date_splitted.append((date_list[i].split(' ')[0].strip()).split('-')) # create a new list with a date splitted as 'year', 'month','day'
            quarter = (((int(date_splitted[i][1]))+2)//3) # calculate the quarter
            writer.writerow([date_pk[i], (date_list[i].split(' ')[0].strip()), date_splitted[i][0], date_splitted[i][1], date_splitted[i][2], day_of_the_week ,str('Q') + str(quarter)])    # write to csv


get_date_csv('dates.csv')