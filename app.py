from flask import Flask

app = Flask(_name_)

@app.route("/")
def hello():
    return "Hello, Azure from Python 3.10!"

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8000)