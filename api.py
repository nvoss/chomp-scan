from flask import Flask, request, render_template, json
import os

app = Flask(__name__, static_url_path='')
server = '0.0.0.0:5000'
chomp_path = ""

@app.route('/')
def status():
    scans = get_scans()
    return render_template('scans.html', scans=scans)

def get_scans():
    files = []
    # r=root, d=directories, f = files
    scans = []
    for r, d, f in os.walk("."):
        for directory in d:
            if '-' in directory:
                scans.append(directory)

    return scans

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)