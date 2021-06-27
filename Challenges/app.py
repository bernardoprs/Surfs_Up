from flask import Flask
app = Flask (_name_)
 
    app.run()



@app.route('/')
def hello_world():
    return 'Hello world'
