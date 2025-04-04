"""
Author: Patan Musthakheem
Date & Time: 20-03-2025 1:59 AM
"""

from flask import Flask, Blueprint, render_template, request, session, send_file, Response

import os
from . import utils
from . import api
from . import generate_heatmap
from . import chat



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
            try:
                file_path = os.path.join(os.path.abspath("uploads"), file.filename)
                file.save(file_path)
                predictor = api.XRayPredictor()
                with open(file_path, "rb") as f:
                    image_bytes = f.read()
                result = predictor.predict(image_bytes)
                # nsure 'prediction' key exists
                disease_detected = result.get('prediction', [None])[0]
                if not disease_detected:
                    return "Error: No disease detected", 400
                # Generate heatmap
                heatmap = generate_heatmap.XRayHeatmapGenerator()
                
                image_bytes = open(file_path, "rb").read()
                heatmap_array = heatmap.generate_heatmap(image_bytes)
                output_path = heatmap.overlay_heatmap(heatmap_array, image_bytes)
                # Generate LLM-based report
                data_llm = chat.GPT().create_prompt(disease_detected)
                data_llm = data_llm.encode("utf-8", errors="replace").decode("utf-8")
                print(data_llm)
                # Generate PDF
                pdf = utils.generate_pdf(file_path, output_path, data_llm)
                response = Response(pdf, content_type="application/pdf")
                response.headers["Content-Disposition"] = f"attachment; filename=report.pdf"
                return response
            except Exception as e:
                return f"Error: {str(e)}", 500
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
