#connect to data source, using userName and userPWD
import csv 
import pyodbc
server = 'tcp:131.114.72.230' 
database = 'Group_ID_137_DB' 
username = 'Group_ID_137' 
password = '********'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()


# Function to populate tables the database
# then just call for example populate_table('gun.csv', sql_query = INSERT...)

def populate_table(input_file, sql_query):
    cnxn = pyodbc.connect(connectionString)
    cursor =cnxn.cursor()
    with open(input_file, 'r',newline = '') as csvfile:
        reader =csv.reader(csvfile)
        next(reader)
        for row in reader:
            cursor.execute(sql_query, *row)
        cnxn.commit()
    cursor.close()



def create_table(input_file, columns, id_name, output_file):
    with open(input_file, 'r', newline='', encoding= 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        with open(output_file, 'w', newline='') as csv_output:
            writer = csv.DictWriter(csv_output,fieldnames= [id_name] + columns)
            writer.writeheader()  # adding the column names (header)
            row_set = set()
            id_count = 0 # counter to create an id
            id_dict = {} # dictionary to assing an id number for every row
            row_dict = {}
            for row in reader:
                row_tuple = tuple(row[column] for column in columns)  # every row will be tuple of each column (column1_value,column2_value)
                if row_tuple not in row_set:  # if this tuple is in the set (no duplicates) id will be assigned and new dictionary created
                    id_count+=1
                    id_dict = {id_name:id_count}  
                    row_set.add(row_tuple)
                    row_dict = dict(zip(columns, row_tuple))   # k: v for k, v in zip(keys, values)   
                    row_dict.update(id_dict) 
                    writer.writerow(row_dict) # create a new csv file 
