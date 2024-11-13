#C:\TTTTTTTT\yolov5_master\yolov5_master
#C:\TTTTTTTT\yolov5_master\yolov5_master\venv\Scripts\python.exe
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'
    
if __name__ == '__main__':
    #app.run('127.0.0.1', 5000, debug=True)
    app.run(debug=True)