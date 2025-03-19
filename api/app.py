from flask import Flask, request

app = Flask("app")

@app.route('/upload-xray')
def upload_xray():

    pass

@app.route("/upload-mri")
def upload_mri():
    pass
