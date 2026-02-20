from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, abort, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfghjkl'
bootstrap = Bootstrap5(app)

projects_data = [
    {"id": 1,
     "title": "Portfolio Site",
     "description": "Built with Flask",
     "tech": "Python, HTML, CSS, Jinja2",
     "github_link": "https://github.com/lkoenigs-2025/HW-1.5",
     "image_url": "https://picsum.photos/seed/picsum/200/300"},
    {"id": 2,
     "title": "Weather App",
     "description": "API Integration",
     "tech": "JavaScript, React, OpenWeatherMap API",
     "github_link": "https://github.com/lkoenigs-2025/HW-1.5",
     "image_url": "https://picsum.photos/200"},
    {"id": 3,
     "title": "To-Do List",
     "description": "Task Management",
     "tech": "JavaScript, Python, CSS, API",
     "github_link": "https://github.com/lkoenigs-2025/HW-1.5",
     "image_url": "https://picsum.photos/200"},
    {"id": 4,
     "title": "Simple Calculator",
     "description": "Math and Logic",
     "tech": "Java, React, JavaScript CSS",
     "github_link": "https://github.com/lkoenigs-2025/HW-1.5",
     "image_url": "https://picsum.photos/200/300/?blur"}
]

class ContactForm(FlaskForm):
    name = StringField('Your Name', validators = [DataRequired()])
    email = StringField('Email Address', validators = [DataRequired(), Email()])
    message = TextAreaField('Message', validators = [DataRequired()])
    submit = SubmitField('Send Message')
@app.route('/')
def index():  # put application's code here
    return render_template('home.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()# put application's code here
    if form.validate_on_submit():
        user_name = form.name.data
        user_email = form.email.data
        user_message = form.message.data
        return redirect(url_for('contact_submission', user_name = user_name, user_email = user_email, user_message = user_message))
    return render_template('contact.html', form=form)

@app.route('/contact_submission/<user_name>/<user_email>/<user_message>')
def contact_submission(user_name, user_email, user_message):
    return render_template('contact.html', user_name=user_name, user_email=user_email, user_message=user_message)
@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/projects')
def projects():   # put application's code here
    return render_template('projects.html', projects = projects_data)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    selected_project = None
    for project in projects_data:
        if project['id'] == project_id:
            selected_project = project
    if not selected_project:
        abort(404)
    return render_template('projects_detail.html', project = selected_project)
if __name__ == '__main__':
    app.run(debug=True)
