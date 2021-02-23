from flask import Flask, render_template, request, redirect, url_for

import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print("Form data received")
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            rec = sr.Recognizer()
            audio = sr.AudioFile(file)
            with audio as src:
                data = rec.record(src)
            text = rec.recognize_google(data, key=None)
            return render_template('index.html', transcript=text)
            print(text)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
