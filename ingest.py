import csv
import sys
import psycopg2

# get data in form of list
def insert(file_name):
    dbconn=psycopg2.connect("dbname=superheros")
    cursor=dbconn.cursor()

    f=open(file_name)
    data=csv.reader(f)
    for name,gender in data:
        cursor.execute("INSERT INTO hero (name,gender) VALUES (%s,%s)",(name,gender))
    dbconn.commit()

def main():
    file=sys.argv[1]
    insert(file)

main()
