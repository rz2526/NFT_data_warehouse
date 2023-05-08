import flask
import datetime
import pandas
import json
import requests



# Initialize Flask HTTP Server
app=flask.Flask(__name__)

@app.route("/query",methods=["GET"])
def query_and_return_table():
    data_dict={"id":[100,101,102],"cont":['abc','ijk','xyz']}
    columns=['id','cont']
    index=['a','b','c']
    df=pandas.DataFrame(data_dict,columns=columns,index=index)
    table=df.to_html(index=False)
    return flask.render_template("index.html",tables=df)

@app.route("/",methods=["GET"])
def index_page():
    return flask.send_file("index.html")