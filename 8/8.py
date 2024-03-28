from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    # Отримати список проектів з бази даних або файлу
    projects_list = [
        {
            'title': 'Сайт',
            'image': 'project1.jpg',
            'technologies': ['Flask', 'HTML', 'CSS', 'JavaScript'],
            'repository_link': 'https://github.com/your_username/project1'
        },
        {
            'title': 'Калькулятор',
            'image': 'project2.jpg',
            'technologies': ['Django', 'React', 'MySQL'],
            'repository_link': 'https://github.com/your_username/project2'
        },
        # Додайте інші проекти за необхідності
    ]
    return render_template('projects.html', projects=projects_list)

@app.route('/project/<int:id>')
def project_details(id):
    # Отримати інформацію про проект з бази даних або файлу
    project_info = {
        'title': 'Іетернет магазин'
        'description': 'Розробляв інтернет магазин в ворк преси'
    }
    return render_template('project_details.html', project=project_info)

if __name__ == '__main__':
    app.run(debug=True)
