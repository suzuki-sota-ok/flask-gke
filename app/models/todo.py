from google.cloud import firestore
import os

PROJECT_ID = os.environ.get('PROJECT_ID')
DATABASE_NAME = os.environ.get('DATABASE_NAME')
db = firestore.Client(
    project=PROJECT_ID,
    database=DATABASE_NAME
)

def get_todos():
    todos_ref = db.collection('todos')
    todos = todos_ref.stream()
    return [{'id': todo.id, 'task': todo.to_dict().get('task')} for todo in todos]

def add_todo(task):
    todos_ref = db.collection('todos')
    todos_ref.add({'task': task})

def delete_todo(todo_id):
    todo_ref = db.collection('todos').document(todo_id)
    todo_ref.delete()