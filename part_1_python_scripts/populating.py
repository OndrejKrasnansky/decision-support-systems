#connect to data source, using userName and userPWD
import csv 
import pyodbc
server = '**********' 
database = 'Group_ID_137_DB' 
username = 'Group_ID_137' 
password = '********'
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
cnxn = pyodbc.connect(connectionString)
cursor = cnxn.cursor()


from functions import populate_table
# populate dates
populate_table(input_file = 'dates.csv', sql_query = "INSERT INTO dates(date_id,date,year,month,day, quarter,day_of_the_week) VALUES(?,?,?,?,?,?,?)") 
#populate gun
populate_table(input_file = 'gun.csv', sql_query = "INSERT INTO gun(gun_id,gun_stolen,gun_type) VALUES(?,?,?)")
#populate participant
populate_table(input_file = 'participant.csv', sql_query = "INSERT INTO participant(participant_id,participant_gender,participant_age_group,participant_status,participant_type) VALUES(?,?,?,?,?)")
#populate geography
populate_table('geography_with_id.csv', sql_query = "Insert INTO geography(geo_id,latitude,longitude,city,state,county) VALUES(?,?,?,?,?,?)")
#populate custody
populate_table('custody.csv',sql_query = "INSERT INTO custody(custody_id,participant_id,gun_id,incident_id,geo_id,date_id,crime_gravity) VALUES(?,?,?,?,?,?,?)")
