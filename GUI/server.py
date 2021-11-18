from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from gcloud import storage
import os

app = Flask(__name__, template_folder=".")
os.environ["GCLOUD_PROJECT"] = "cloud-hw4-332302"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cloud-hw4-332302-caa08fee8d9d.json"
BUCKET = "dataproc-staging-us-central1-875447532611-uunco0qf"


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/uploader", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        client = storage.Client()
        bucket = client.get_bucket(BUCKET)

        f = request.files["file"]
        blob = bucket.blob(f.filename)
        f.save(secure_filename(f.filename))
        blob.upload_from_filename(f.filename)

        return "<h1>File uploaded successfully</h1>"


if __name__ == "__main__":
    app.run(debug=False)
