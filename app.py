from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQALCHEMY_TRACK_MODIFICATIONS '] = False
db= SQLAlchemy(app)

class ToDo(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(100))
	complete = db.Column(db.Boolean)

@app.route('/')
def find():
	todolist=ToDo.query.all()
	print(todolist)
	return render_template("base.html",todoitems = todolist)

@app.route('/submit',methods=['POST'])
def add():
	title = request.form.get("name")
	with app.app_context():
		new_todo = ToDo(title=title,complete=False)
		db.session.add(new_todo)
		db.session.commit()
	return redirect(url_for("find"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
	todo = ToDo.query.filter_by(id=todo_id).first()
	todo.complete = not todo.complete
	db.session.commit()
	return redirect(url_for("find"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
	todo = ToDo.query.filter_by(id=todo_id).first()
	db.session.delete(todo)
	db.session.commit()
	return redirect(url_for("find"))



app.add_url_rule('/home','home',home)




if __name__ == "__main__":
	
	app.run(debug=True)
	


