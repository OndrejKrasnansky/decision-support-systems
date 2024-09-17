from functions import create_table
import csv
#create_table(input_file, columns, id_name, output_file)

create_table(r'C:\Users\ondre\Documents\UNIPI updated\UNIPI\Second Year\Laboratory for DS\LDS_Project_2023\LDS_Group_ID_137\files .py\Police.csv', ['participant_age_group','participant_gender','participant_status','participant_type'], 'participant_id', 'participant.csv')
create_table(r'C:\Users\ondre\Documents\UNIPI updated\UNIPI\Second Year\Laboratory for DS\LDS_Project_2023\LDS_Group_ID_137\files .py\Police.csv', ['gun_stolen','gun_type'], 'gun_id', 'gun.csv')
create_table(r'C:\Users\ondre\Documents\UNIPI updated\UNIPI\Second Year\Laboratory for DS\LDS_Project_2023\LDS_Group_ID_137\files .py\Police.csv',['latitude', 'longitude'], 'geo_id', 'geography.csv')

