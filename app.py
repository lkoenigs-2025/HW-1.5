from flask import Flask, render_template, abort

app = Flask(__name__)

projects_data = [
    {"id": 1,
     "title": "Portfolio Site",
     "description": "Built with Flask",
     "tech": "Python, HTML, CSS, Jinja2",
     "github_link": "[https://github.com/](https://github.com/)...",
     "image_url": "[https://picsum.photos/id/1/600/400](https://picsum.photos/id/1/600/400)"},
    {"id": 2,
     "title": "Weather App",
     "description": "API Integration",
     "tech": "JavaScript, React, OpenWeatherMap API",
     "github_link": "[https://github.com/](https://github.com/)...",
     "image_url": "[https://picsum.photos/id/10/600/400](https://picsum.photos/id/10/600/400)"},
    {"id": 3,
     "title": "To-Do List",
     "description": "Task Management",
     "tech": "JavaScript, React, OpenWeatherMap API",
     "github_link": "[https://github.com/](https://github.com/)...",
     "image_url": "[https://picsum.photos/id/10/600/400](https://picsum.photos/id/10/600/400)"},
    {"id": 4,
     "title": "Simple Calculator",
     "description": "Math and Logic",
     "tech": "JavaScript, React, OpenWeatherMap API",
     "github_link": "[https://github.com/](https://github.com/)...",
     "image_url": "[https://picsum.photos/id/10/600/400](https://picsum.photos/id/10/600/400)"}
]
@app.route('/')
def index():  # put application's code here
    return render_template('home.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/projects')
def projects(projects_data):   # put application's code here
    return render_template('projects.html', projects = projects_data)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    for project in projects_data:
        if project['id'] == project_id:
            selected_project = project
        if not selected_project:
            abort(404)
    return render_template('projects_detail.html', project = selected_project)
if __name__ == '__main__':
    app.run()
