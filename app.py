from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return f"Welcome, {user}!"
    return render_template('login.html')
