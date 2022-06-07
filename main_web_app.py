#Author: Palumbo Raffaele
#Date: 2022
from typing import Type
from flask import Flask, render_template, request, redirect, url_for
from connector import show_databases, use_database

web_app = Flask(__name__)
##########
user_id = 'root'
pw = 'abc'
##########

@web_app.route('/') 
def index():
    return render_template('main.html')

@web_app.route('/sql',methods=["GET","POST"])
def sql_page():
    db_list = show_databases(user_id,pw)
    db_name = request.form.get('db_name')
    if request.method == "POST":
        try:
            tables = use_database(str(db_name))
            len_list = len(tables)
            message ='Database successfully loaded'
            #redirect(url_for('sql_manipulator'))
            #return sql_manipulator(db_name = db_name, len_list = len_list, message = message)
            return render_template('db_manipulator.html', message = message, db_name = db_name, tables = tables, len_list = len_list)
        except:
            return render_template('error_loading.html')
    return render_template('sql_form.html',db_list = db_list, user_id = user_id)

#This function will allow multiple manipulations, beginning from
#to show a defined table
#add and remove data from MariaDB
# @web_app.route('/sql_manipulator',methods=["GET","POST"])
# def sql_manipulator(db_name, len_list, message):
#     tables = use_database(str(db_name))
#     table = request.form.get('table')
#     print(table)
#     return render_template('db_manipulator.html', message = message, db_name = db_name, tables = tables, len_list = len_list)


if __name__ == '__main__':
    web_app.run(debug=True)