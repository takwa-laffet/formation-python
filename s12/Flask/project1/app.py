from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
app=Flask(__name__) 

@app.route("/")
def home():
    return "hi this is me"
@app.route("/contact")
def f1():
    return "contact"
@app.route("/about")
def f2():
    return "about"
@app.route("/user/<name>")
def f3(name):
    return f"hello {name}"
@app.route("/age/<int:age>")
def f4(age):
    return f"your age is {age}"
@app.route("/test")
def f5():
    return "<h1>hello</h1>"
@app.route("/page")
def page():
    return render_template("index.html",name="ali")
@app.route("/produit")
def produit():
    produits=["hp","dell","lenovo","asus","msi"]
    return render_template("produit.html",produits=produits)

@app.route("/api/username",methods=["GET","POST"])
def username():
    if request.method=="POST":
        username=request.form["username"]
        return f"hello {username}"
    else:
        return render_template("form.html")
@app.route("/serche")
def serche():
    id=request.args.get("id")
    return f"this is {id}"
#api json
@app.route('/posts')
def posts():
    return jsonify([
        {
            'id': 1,
            'title': 'First Post',
            'content': 'First Post Content'
        },
        {
            'id': 2,
            'title': 'Second Post',
            'content': 'Second Post Content'
        },
        {
            'id': 3,
            'title': 'Third Post',
            'content': 'Third Post Content'
        }
    ])
if __name__ == "__main__":
    app.run(debug=True)
