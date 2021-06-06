import csv
import sys
import psycopg2

def dump(fname):
    dbconn=psycopg2.connect("dbname=superheros")
    cursor=dbconn.cursor()
    f=open(fname,"w")
    reader=csv.writer(f)
    cursor.execute("SELECT name,gender from hero")
    for name,gender in cursor.fetchall():
        # print(name,gender)
         reader.writerow([name,gender])
    dbconn.commit()
    f.close()

def main():
    fname=sys.argv[1]
    dump(fname)
main()