# Decision-Support-Systems

Repository Contains

	
 
	- Part_1_python_scripts:
  	  - create_tables.py
  	  - dates.py
  	  - fact_table.py
  	  - functions.py
      - populating.py
         
	- Part_2_ETL 
 
	- Part_3_OLAP_MDX
 
	- Project Report


Part 1: DataWarehouse building:

- In this part the repository contain 4 different python notebooks which were used to preprocess and create separated tables to build an efficient datawarehouse tables (**create_tables.py**)
- **dates.py** works to parse XML file to CSV and create the table 'dates'
- **fact_table.py** is a final script which creates a central fact table for a star schema of the datawarehouse. This script requieres all tables already done and created.
- **fact_table.py** includes functions : create_tables and populate_table
- **populating.py** connects to the server using pyodbc and populate the already created star schema in **SSMS**
