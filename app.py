from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, abort, request


app = Flask(__name__)
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
@app.route('/')
def index():  # put application's code here
    return render_template('home.html')

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
