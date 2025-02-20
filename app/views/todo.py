from flask import Blueprint, render_template, request, redirect, url_for
from app.models import get_todos, add_todo, delete_todo

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            add_todo(task)
        return redirect(url_for('todo.todo'))
    
    todos = get_todos()
    return render_template('todo.html', todos=todos)

@todo_bp.route('/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    delete_todo(todo_id)
    return redirect(url_for('todo.todo'))