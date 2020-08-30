
#test file
DF_SHORT = INF_DF[['longName','ask']]

#Create database
import sqlite3

#create SQL datbase
db_sql = sqlite3.connect("/Users/JZ/Downloads/Databases/test_database5.db")
sql = db_sql.cursor()

#create table and define columns
sql.execute(
    """
    CREATE TABLE test (
        ask INTEGER ,
        longName TEXT NOT NULL,
        PRIMARY KEY(ask)
        );
     """
)
