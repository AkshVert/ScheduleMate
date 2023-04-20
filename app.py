from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task = request.form['task']
        date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        tasks.append((task, date))
        return 'Task added successfully!'
    else:
        return render_template('home.html')

@app.route('/reminders', methods=['POST'])
def reminders():
    action = request.form['action']
    today = datetime.now().date()
    reminders = [(task, date.strftime('%Y-%m-%d')) for task, date in tasks if date.date() == today]
    if action == 'today':
        return render_template('reminders.html', reminders=reminders)

if __name__ == '__main__':
    app.run(debug=True)
