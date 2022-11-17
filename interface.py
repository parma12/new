from flask import Flask, jsonify, render_template, request

from Project_app.utils import MedicalInsurance

app  = Flask(__name__)
###########################################################################################
############################### Base API ##################################################
###########################################################################################
@app.route("/") # HOME API
def hello_flask():
    print("Welcome to flask")
    return "Hello Python"


###########################################################################################

@app.route("/predict_charges")
def get_insurance_charges():
    age = 26
    sex ='female'
    bmi = 26.5
    children = 1
    smoker  = 'yes'
    region = 'southwest'

    med_ins = MedicalInsurance(age,sex, bmi,children,smoker,region)
    charges = med_ins.get_predicted_charges()
    return jsonify ({"Result": f"Predicted medical insurance charges are:{charges}"})




if __name__ == "__main__":
    app.run()