"""
Author: Patan Musthakheem
Date & Time: 20-03-2025 1:59 AM
"""

from flask import Flask, Blueprint, render_template, request, session

import os
import api

routes = Blueprint("routes", __name__)

@routes.route("/", methods=["GET"])
def index():
    return render_template("home.html")

@routes.route("/admin-login")
def admin_login():
    return render_template("admin-login.html")

@routes.route("/admin-dashboard", methods=["POST"])
def admin_dashboard():
    # TODO
    return render_template("admin-dash.html")





# For Doctor

@routes.route("/doctor-login")
def doctor_login():
    return render_template('doc-login.html')

@routes.route("/doctor-login/doctor-dashboard", methods=["POST"])
def doctor_dashboard():
    try:
        doctor_id = request.form['doctorId']
        doctor_pass = request.form['doctorPass']
        if doctor_id == "mahima" and doctor_pass == "mahima":
            session['LOGGED_IN'] = True
            return render_template("doc-dash.html")            
    except Exception:
        raise
        # return render_template("error.html", message="Error Occured")
    return render_template("error.html", message="Enter Correct Password & Doctor ID")

@routes.route("/doctor-login/doctor-dashboard/doctor-upload-xray", methods=["GET", "POST"])
def doctor_upload_xray():
    if not session.get('LOGGED_IN'):
        return render_template("error.html", message="Please Log In First")
    if request.method == "GET":
        return render_template("doc-upload.html")
    else:
        # TODO load the file
        if 'file' not in request.files:
            return "No File found"
        file = request.files['file']
        if file.filename == '':
            return "No Selected File"
        if file:
            file_path = os.path.join("uploads", file.filename)
            file.save(file_path)
            # TODO PREDICT AND GENERATE REPORT AND SEND BACK
            
            data: dict
            # TODO
            
        return render_template("generate-report.html", data=data)


@routes.route("/doctor-login/doctor-dashboard/doctor-upload-mri", methods=["GET", "POST"])
def doctor_upload_mri():
    if not session.get('LOGGED_IN'):
        return render_template("error.html", message="Please Log In First")
    if request.method == "GET":
        return render_template("doc-upload.html")
    else:
        # TODO load the file
        if 'file' not in request.files:
            return "No File found"
        file = request.files['file']
        if file.filename == '':
            return "No Selected File"
        if file:
            file_path = os.path.join("uploads", file.filename)
            file.save(file_path)
            # TODO PREDICT AND GENERATE REPORT AND SEND BACK
            data: dict
            # TODO
            
        return render_template("generate-report.html", data=data)




# For Patient

@routes.route("/patient-login")
def patient_login():
    return render_template("patient-login.html")

@routes.route("/patient-login/patient-dashboard", methods=["POST"])
def patient_dashboard():
    patient_id = request.form.get("patientID")
    patient_pass = request.form.get("patientPASS")
    if not patient_id or not patient_pass:
        return render_template("error.html", message="Error!")
    if patient_id == 'mahima' and patient_pass == 'mahima':
        return render_template('patient-dash.html')
    return render_template("error.html", message="Please enter correct patient credintials!")
