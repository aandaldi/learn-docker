from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Flask!"

@app.route('/cobafolder')   #mapping
def folder():
    return "Ini Folder Yah" 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') #untuk mengaktifkan debug