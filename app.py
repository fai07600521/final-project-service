# Import libraries
from pprint import pprint
from flask import Flask, request, jsonify, render_template,redirect
import dnnlib
import pickle
import torch 
import dill
import os
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from generate import generate_images
from style_mixing import generate_style_mix
import base64
import glob
from pprint import pprint
import joblib
import sys 
pprint(sys.argv[1])

app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'fask'

mysql = MySQL(app) 

PEOPLE_FOLDER = os.path.join('static', 'faminine')
# import pretrained_networks
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
  
@app.route('/',methods=["GET", "POST"])
def home(name=None):
        return render_template('home.html')

@app.route('/mixingStyle',methods=["GET", "POST"])
def mixingStyle(name=None):
         pprint("getttti innnnn33")
         if request.method == "POST":
           pprint("getttti innnnn11")
           pprint(request.form)
           pprint(request.form.get("classy"))
           if request.form.get("classy"):
                    pprint("getttti classy")
                   # picklePath = r"D:\New folder (3)\picker-files\classy\network-snapshot-001370.pkl"
                   # generate_mixstyle_img(picklePath)
                    return render_template('mixingStyle.html') 
         elif request.form.get("faminine"):
                    pprint("getttti faminine")
                    picklePath = r"D:\New folder (3)\picker-files\faminine\network-snapshot-000960.pkl"
                    generate_mixstyle_img(picklePath)
                    return render_template('mixingStyle.html',style=request.form.get("faminine")) 
         elif request.form.get("masculine"):
                    pprint("getttti masculine")
                    picklePath = r"D:\New folder (3)\picker-files\masculine\new\network-snapshot-000440.pkl"
                    generate_mixstyle_img(picklePath)
                    return render_template('mixingStyle.html',style=request.form.get("masculine")) 
         elif request.form.get("street"):
                    pprint("getttti streetstreet")
                    picklePath = r"D:\New folder (3)\picker-files\street\network-snapshot-000600.pkl"
                    generate_mixstyle_img(picklePath)
                    return render_template('mixingStyle.html',style=request.form.get("street")) 
         elif request.form.get("minimal"):
                    picklePath = r"D:\New folder (3)\picker-files\minimal\network-snapshot-002145.pkl"
                    generate_mixstyle_img(picklePath)
                    return render_template('mixingStyle.html',style=request.form.get("minimal")) 
         else:

                #    picklePath = r"D:\New folder (3)\picker-files\sexy\network-snapshot-003556.pkl"
                #    generate_mixstyle_img(picklePath)
                    return render_template('mixingStyle.html') 

folderImg = r"D:\New folder (3)\folderImg\Data"
imagelist = []
@app.route('/generated',methods=["GET", "POST"])
def generated(name=None):
    if request.method == "POST":
         if request.form.get("classy"):
                    pprint("classyyyyy")
                    network_pkl = r"D:\New folder (3)\picker-files\classy\network-snapshot-001370.pkl"
                    file = open("./network-snapshot-001370.pkl","rb")
                    #load trained model
                    trained_model = joblib.load(file)
                    pprint(trained_model)
                    generate_img(trained_model)
                    return render_template('indexx.html',style=request.form.get("classy")) 
         elif request.form.get("faminine"):
                    pprint("faminineeeee")
                    network_pkl = r"D:\New folder (3)\picker-files\faminine\network-snapshot-000960.pkl"
                    generate_img(network_pkl)
                    return render_template('indexx.html',style=request.form.get("faminine")) 
         elif request.form.get("masculine"):
                    pprint("masculineeee")
                    network_pkl = r"D:\New folder (3)\picker-files\masculine\new\network-snapshot-000440.pkl"
                    generate_img(network_pkl)
                    return render_template('indexx.html',style=request.form.get("masculine")) 
         elif request.form.get("street"):
                    pprint("streettttt")
                    network_pkl = r"D:\New folder (3)\picker-files\street\network-snapshot-000600.pkl"
                    generate_img(network_pkl)
                    return render_template('indexx.html',style=request.form.get("street")) 
         elif request.form.get("minimal"):
                    pprint("minimalllll")
                    network_pkl = r"D:\New folder (3)\picker-files\minimal\network-snapshot-002145.pkl"
                    generate_img(network_pkl)
                    return render_template('indexx.html',style=request.form.get("minimal")) 
         else:
                    pprint("sexyyyy")
                    network_pkl = r"D:\New folder (3)\picker-files\sexy\network-snapshot-003556.pkl"
                    generate_img(network_pkl)
                    return render_template('indexx.html',style=request.form.get("sexy")) 


     
def generate_img(network_pkl):
    randomlist = []
    noise_mode = None
    for i in range(0,45):
        n = random.randint(1, 99999)
        randomlist.append(n)
    generate_images(
        network_pkl,
        randomlist,
        folderImg,
        noise_mode,
        None,
        None,
        1
)

def generate_mixstyle_img(network_pkl):
    row_seeds = []
    for i in range(0,6):
        n = random.randint(1, 99999)
        row_seeds.append(n)
    col_seeds = []
    for i in range(0,6):
        n = random.randint(1, 99999)
        col_seeds.append(n)
    generate_style_mix(
        folderImg,
        network_pkl,  
    )



if __name__ == '__main__':
    app.run(threaded=False, debug=False, host='127.0.0.1', port=5000)
    

