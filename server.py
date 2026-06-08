from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return "LMS File Server Running"


@app.route("/upload", methods=["POST"])
def upload_file():

    if "file" not in request.files:
        return jsonify({
            "success": False,
            "message": "No file found."
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "message": "No filename selected."
        }), 400

    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    # Prevent overwriting existing files
    if os.path.exists(filepath):

        name, ext = os.path.splitext(filename)
        counter = 1

        while True:
            new_filename = f"{name}_{counter}{ext}"
            filepath = os.path.join(
                UPLOAD_FOLDER,
                new_filename
            )

            if not os.path.exists(filepath):
                filename = new_filename
                break

            counter += 1

    file.save(filepath)

    return jsonify({
        "success": True,
        "filename": filename
    })


@app.route("/files", methods=["GET"])
def get_files():

    files = os.listdir(UPLOAD_FOLDER)

    return jsonify(files)


@app.route("/download/<filename>", methods=["GET"])
def download_file(filename):

    return send_from_directory(
        UPLOAD_FOLDER,
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )