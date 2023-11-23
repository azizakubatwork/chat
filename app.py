from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data structure to store room information
rooms = {
    'room1': {'name': 'Room 1', 'messages': []},
    'room2': {'name': 'Room 2', 'messages': []},
    'room3': {'name': 'Room 3', 'messages': []},
}


@app.route('/')
def home():
    return render_template('home.html', rooms=rooms)


@app.route('/room/<room_name>', methods=['GET', 'POST'])
def room(room_name):
    if request.method == 'POST':
        username = request.form['username']
        if not username or len(username) > 50:
            return redirect(url_for('home'))

        # Assuming you have a message list associated with each room
        if room_name not in rooms:
            rooms[room_name] = {'messages': []}

        return render_template('room.html', room_name=room_name, username=username, messages=rooms[room_name]['messages'])

    return render_template('room.html', room_name=room_name)


@app.route('/leave/<room_name>/<username>')
def leave(room_name, username):
    # Clean up resources or perform any necessary actions when leaving
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
