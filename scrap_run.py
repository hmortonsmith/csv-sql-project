import csv
import pyodbc


# PART I
IMDB_py_data = []
with open('IMDB.csv', newline='') as csv_file:
    IMDB_csv = csv.reader(csv_file, delimiter=',')

    for row in IMDB_csv:
        individual_row = []
        individual_row.append(row[0])
        individual_row.append(row[1].replace("'", "''"))
        individual_row.append(row[2].replace("'", "''"))
        individual_row.append(row[3])

        if 'N' in row[4]:
            individual_row.append(0)
        else:
            individual_row.append(row[4])

        if 'N' in row[5]:
            individual_row.append(0)
        else:
            individual_row.append(row[5])

        if 'N' in row[6]:
            individual_row.append(0)
        else:
            individual_row.append(row[6])
        individual_row.append(row[7])
        IMDB_py_data.append(individual_row)

# PART II
# Connect to DB
server = 'localhost,1433'
database = 'IMDB'
username = 'SA'
password = 'Passw0rd2018'

# Making a connection
IMDB_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+'')

# Creating a cursor allowing me to execute SQL functions through my connection
cursor = IMDB_conn.cursor()

# PART III
# Add a table to Database (Created DB in SQL
#cursor.execute("CREATE TABLE IMDB_Movies (VideoType VARCHAR(20), PrimaryTitle VARCHAR(70), OriginalTitle VARCHAR(70), IsAdult BIT, StartYear SMALLINT, EndYear SMALLINT, RunTime SMALLINT, Genres VARCHAR(70));")

# Add IMDB data to table in SQL DB
# For each list within my list run an iteration
# and run a SQL statement on that inner list (or row) adding it to my newly created table
for entry in IMDB_py_data[1:]:
    print(entry)
    #cursor.execute(f"INSERT INTO IMDB_Movies (VideoType, PrimaryTitle, OriginalTitle, IsAdult, StartYear, EndYear, RunTime, Genres) VALUES ('{entry[0]}', '{entry[1]}', '{entry[2]}', '{entry[3]}' , '{entry[4]}' , '{entry[5]}', '{entry[6]}', '{entry[7]}');")


# Commit my changes to the SQL database
#IMDB_conn.commit()
