
import json
import csv

j_age = open(r'C:\Users\ondre\Documents\UNIPI updated\UNIPI\Second Year\Laboratory for DS\LDS_Project_2023\LDS_Group_ID_137\files .py\dict_partecipant_age.json')
j_status = open(r'C:\Users\ondre\Documents\UNIPI updated\UNIPI\Second Year\Laboratory for DS\LDS_Project_2023\LDS_Group_ID_137\files .py\dict_partecipant_status.json')
j_type = open(r'C:\Users\ondre\Documents\UNIPI updated\UNIPI\Second Year\Laboratory for DS\LDS_Project_2023\LDS_Group_ID_137\files .py\dict_partecipant_type.json')

d_age = json.load(j_age)
d_status  = json.load(j_status)
d_type = json.load(j_type)

print(d_age)
print(d_status)
print(d_type) # crime_gravity value when the person is victim will be 0 for all rows 


j_age.close()
j_status.close()
j_type.close()


with open(r'C:\Users\ondre\Documents\UNIPI updated\UNIPI\Second Year\Laboratory for DS\LDS_Project_2023\LDS_Group_ID_137\files .py\gun.csv','r',newline ='') as guncsv, \
open(r'C:\Users\ondre\Documents\UNIPI updated\UNIPI\Second Year\Laboratory for DS\LDS_Project_2023\LDS_Group_ID_137\files .py\geography_with_id.csv','r',newline ='', encoding='utf-8') as geocsv,\
open(r'C:\Users\ondre\Documents\UNIPI updated\UNIPI\Second Year\Laboratory for DS\LDS_Project_2023\LDS_Group_ID_137\files .py\participant.csv','r',newline ='', encoding='utf-8') as participantcsv,\
open(r'C:\Users\ondre\Documents\UNIPI updated\UNIPI\Second Year\Laboratory for DS\LDS_Project_2023\LDS_Group_ID_137\files .py\Police.csv','r', newline ='') as policecsv:
    gun = csv.DictReader(guncsv)
    geo = csv.DictReader(geocsv)
    participant = csv.DictReader(participantcsv)
    police = csv.DictReader(policecsv)
    with open('custody.csv','w',newline='') as factcsv:
        columns = ['custody_id','participant_id','gun_id','incident_id','geo_id','date_id', 'crime_gravity']
        writer = csv.DictWriter(factcsv, fieldnames = columns)
        writer.writeheader()
        gun_tuple = tuple()
        gun_id_dict ={}
        geo_id_dict ={}
        part_id_dict = {}

        for row in gun:
            gun_id_dict[row['gun_stolen'], row['gun_type']] = row['gun_id']
        
        for row in geo:
            geo_id_dict[row['latitude'], row['longitude']] = row['geo_id']
        
        for row in participant:
            part_id_dict[row['participant_gender'],row['participant_type'],row['participant_status'],row['participant_age_group']] =  row['participant_id']



        for row in police:
            crime_gravity = d_type[row['participant_type']] * d_status[row['participant_status']] * d_age[row['participant_age_group']]
            gun_id = gun_id_dict[(row['gun_stolen'], row['gun_type'])]
            geo_id = geo_id_dict[(row['latitude'], row['longitude'])]
            part_id = part_id_dict[(row['participant_gender'], row['participant_type'], row['participant_status'], row['participant_age_group'])]
            incident_id = row['incident_id']
            custody_id = row['custody_id']
            date_id = row['date_fk']
            writer.writerow({'custody_id': custody_id, 'participant_id': part_id, 'gun_id': gun_id, 'incident_id': incident_id, 'geo_id': geo_id, 'date_id': date_id, 'crime_gravity': crime_gravity })
