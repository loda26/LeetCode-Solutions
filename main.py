from flask import Flask, render_template, request, redirect
from models.users import Users, Session

app = Flask(__name__)

session = Session()

@app.route('/loda')
def index():
    users = session.query(Users).all()
    return render_template('index.html', users=users)

@app.route('/loda/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    user = Users(name=name, email=email, password=password)
    session.add(user)
    session.commit()

    return redirect('/loda')

@app.route('/loda/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = session.query(Users).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        return "User deleted successfully", 200
    else:
        return "User not found", 404

if __name__ == '__main__':
    app.run(debug=True)
