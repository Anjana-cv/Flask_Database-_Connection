from flask import Flask, render_template_string, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registrations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Registration eddda
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<Registration {self.name}>'

# HTML template registration enday
form_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Registration</title>
</head>
<body>
    <h1>Course Registration Form</h1>
    <form action="/" method="POST">
        <label for="name">Full Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="course">Course:</label>
        <select id="course" name="course" required>
            <option value="Web Development">Web Development</option>
            <option value="Data Science">Data Science</option>
            <option value="Machine Learning">Machine Learning</option>
        </select>
        
        <label for="phone">Phone Number:</label>
        <input type="text" id="phone" name="phone" required>
        
        <button type="submit">Register</button>
    </form>

    <p><a href="{{ url_for('view_registrations') }}">View Registered Participants</a></p>
</body>
</html>
'''

# HTML template  result enday
registrations_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registered Participants</title>
</head>
<body>
    <h2>Registered Participants</h2>
    <ul>
        {% for registration in registrations %}
            <li>{{ registration.name }} - {{ registration.email }} - {{ registration.course }} - {{ registration.phone }}
                <a href="{{ url_for('delete_registration', id=registration.id) }}">Delete</a>
            </li>
        {% endfor %}
    </ul>
    <p><a href="{{ url_for('index') }}">Back to Registration Form</a></p>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']
        phone = request.form['phone']
        
        # Add new registration db el akkan
        new_registration = Registration(name=name, email=email, course=course, phone=phone)
        db.session.add(new_registration)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template_string(form_template)

@app.route('/registrations')
def view_registrations():
    registrations = Registration.query.all()
    return render_template_string(registrations_template, registrations=registrations)

@app.route('/delete/<int:id>')
def delete_registration(id):
    registration_to_delete = Registration.query.get_or_404(id)
    db.session.delete(registration_to_delete)
    db.session.commit()
    return redirect(url_for('view_registrations'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
# this code is done by Marapatty Anjana
