import csv
import pyodbc


# PART I
IMDB_py_data = []
with open('IMDB.csv', newline='') as csv_file:
    IMDB_csv = csv.reader(csv_file, delimiter=',')

    for row in IMDB_csv:
        individual_row = []
        individual_row.append(row[0])
        individual_row.append(row[1].replace("'", " "))
        individual_row.append(row[2].replace("'", " "))

        if row[3] == 0:
            individual_row.append('No')
        else:
            individual_row.append('Yes')

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


# for entry in IMDB_py_data[1:]:
#     print(entry[1:2])

# PART II
# Connect to DB
server = 'localhost,1433'
database = 'IMDB'
username = 'SA'
password = 'Passw0rd2018'

# Making a connection
IMDB_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+'')

# Creating a cursor allowing us to execute SQL functions on connected db
cursor = IMDB_conn.cursor()

# PART III
# Add a table to Database (Created DB in SQL
cursor.execute("CREATE TABLE IMDB_Movies (VideoType VARCHAR(100), PrimaryTitle VARCHAR(70), OriginalTitle VARCHAR(70), IsAdult VARCHAR(50), StartYear INT, EndYear INT, RunTime INT, Genres VARCHAR(70));")

# Add IMDB data to table in SQL DB
for entry in IMDB_py_data[1:]:

    cursor.execute(f"INSERT INTO IMDB_Movies (VideoType, PrimaryTitle, OriginalTitle, IsAdult, StartYear, EndYear, RunTime, Genres) VALUES ('{entry[0]}', '{entry[1]}', '{entry[2]}', '{entry[3]}' , '{entry[4]}' , '{entry[5]}', '{entry[6]}', '{entry[7]}');")

IMDB_conn.commit()