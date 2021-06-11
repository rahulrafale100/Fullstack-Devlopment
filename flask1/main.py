from flask import Flask,request
import psycopg2

app=Flask("Job sites")

dbconn=psycopg2.connect("dbname=naukri")
@app.route("/")
def intro():
    
    cursor=dbconn.cursor()
    cursor.execute("select count(*) from openings")
    n=cursor.fetchall()[0][0]
    return f"""
    <html>
    <head>
    <title>Welcome to my page</title>
    </head>
    <body>
    <h1>This is my list of job collection</h1>
    There are currently {n} jobs available.</br>
    Link to the page of jobs is <a href="/jobs">here</a>. 
    </body>
    </html>
    """


@app.route("/jobs")   # Decorator
def hello():
    
    cursor=dbconn.cursor()
    cursor.execute("select title ,company_name,description from openings")
    ret=[]
    for title,company_name,description in cursor.fetchall():
        item=f"<b> {title}</b> :: {company_name} </br> {description}"
        ret.append(item)
    l="<hr/>".join(ret)
    return f"List of Jobs </br>{l}"





# # http://127.0.0.1/add?item=x
# @app.route("/add")
# def adding():
#     item =request.args.get("item")
#     l.append(item)
#     return f"Content in list is {len(l)}"

