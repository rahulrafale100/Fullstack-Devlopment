import random
from flask import Flask,request
from flask import render_template 
import estimator

app=Flask("Webapp1")

@app.route("/")
def intro():
    return render_template("intro.html")

@app.route("/estimate",methods=["POST"])
def estimate():
    algorithm=request.form['algorithm']
    iteration=request.form['iteration']
    if(algorithm=="wallis"):
        estimate=estimator.estimate_wallis(int(iteration))
    elif(algorithm=='monte'):
        estimate=estimator.estimate_monte(int(iteration))
    name={"monte":"Monte Carlo Estimation","wallis":"Wallis Product Estimation"}
    return render_template("estimate.html",algorithm=name[algorithm],iters=iteration,estimate=estimate)

if(__name__=="__main__"):
    app.run()



