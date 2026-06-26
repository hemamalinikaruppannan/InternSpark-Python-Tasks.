from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary data storage (In-memory database)
todos = [
    {"id": 1, "task": "Learn Flask fundamentals", "done": False},
    {"id": 2, "task": "Build Task 4 for InternSpark", "done": True}
]

@app.route('/')
def index():
    # Displays the main page and sends the 'todos' list to the HTML template
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    # Takes the new task typed into the form and adds it to our list
    task_name = request.form.get('task')
    if task_name:
        new_id = len(todos) + 1 if todos else 1
        todos.append({"id": new_id, "task": task_name, "done": False})
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>')
def toggle(todo_id):
    # Switches a task between "Done" and "Undo"
    for todo in todos:
        if todo['id'] == todo_id:
            todo['done'] = not todo['done']
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    # Removes a task completely from the list
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)