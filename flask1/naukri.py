import requests
import bs4 
import psycopg2
import sys

def fetch_jobs():
    url="https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_key_loc&searchType=adv&keyword=python&location=bangalore&k=python&l=bangalore&seoKey=python-jobs-in-bangalore&src=jobsearchDesk&latLong="
    headers={"appid":"109","systemid":"109"}
    r=requests.get(url,headers=headers)
    data=r.json()
    return data["jobDetails"]

def insert_job(jobs):
    dbconn=psycopg2.connect("dbname=naukri")
    cursor=dbconn.cursor()
    for i in jobs:
        title=i['title']
        job_id=i['jobId']
        company_name=i['companyName']
        url=i['jdURL']
        soup=bs4.BeautifulSoup(i['jobDescription'],features="html.parser")
        jd=str(soup.text)
        cursor.execute("""INSERT INTO openings (title,job_id,company_name,url,description) VALUES (%s,%s,%s,%s,%s)""",(title,job_id,company_name,url,jd))
        dbconn.commit()


def create_database():
    dbconn=psycopg2.connect("dbname=naukri")
    cursor=dbconn.cursor()
    f=open("jobs.sql")
    sql_code=f.read()
    f.close()
    cursor.execute(sql_code)
    dbconn.commit()

def main(arg):
    if(arg=="create"):
        create_database()
    elif(arg=="crawl"):
        jobs=fetch_jobs()
        insert_job(jobs)
    else:
        print("Invalid Command!!!!!!!!!!!")

if(__name__=="__main__"):        # This is called import gaurd
    main(sys.argv[1])
