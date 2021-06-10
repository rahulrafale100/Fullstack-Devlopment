from flask import Flask,request
import psycopg2

app=Flask("Job sites")

@app.route("/")   # Decorator
def hello():
    dbconn=psycopg2.connect("dbname=naukri")
    cursor=dbconn.cursor()
    cursor.execute("select title ,company_name,description from openings")
    ret=[]
    for title,company_name,description in cursor.fetchall():
        item=f"<b> {title}</b> :: {company_name} </br> {description}"
        ret.append(item)
    l="<hr/>".join(ret)
    return f"List of Jobs {l}"





# # http://127.0.0.1/add?item=x
# @app.route("/add")
# def adding():
#     item =request.args.get("item")
#     l.append(item)
#     return f"Content in list is {len(l)}"

