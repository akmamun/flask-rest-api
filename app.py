from flask import Flask, jsonify, request

app = Flask(__name__)

todo_list = [
    {
        'id': 1,
        'text': 'this is todo',
        'body': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
        'status': 'Done'
    },
    {
        'id': 2,
        'text': 'this is second todo',
        'body': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
        'status': 'Pending'
    }
]


@app.route('/api/todo/todos', methods=['GET'])
def get_todos():
    return jsonify(todo_list)


@app.route('/api/todo/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = [todo for todo in todo_list if todo['id'] == todo_id]
    if len(todo) == 0:
        return "404 Not Found This todo"
    return jsonify({'todo': todo[0]})


@app.route('/api/todo/todos/create', methods=['GET', 'POST'])
def create_todo():
    if not request.json or not 'text' in request.json:
        return "Todo text in required field"
    else:
        todo = {
            'id': todo_list[-1]['id'] + 1,
            'text': request.json['text'],
            'body': request.json['body'],
            'status': request.json['status'],
        }
    todo_list.append(todo)
    return jsonify({'todo': todo}), 201


@app.route('/api/todo/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = [todo for todo in todo_list if todo['id'] == todo_id]
    if len(todo) == 0:
        return "404 Not Found This todo"
    todo_list.remove(todo[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
