from flask import Flask, render_template, request, flash, jsonify,url_for, redirect
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'panasabotlasreenivas@gmail.com'
app.config['MAIL_PASSWORD'] = 'qlxxgqilaexieurn'  # Use Gmail App Password

mail = Mail(app)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        msg = Message('Portfolio Contact Form',
                      sender='sreenivasulupanasabotla@gmail.com',
                      recipients=['sreenivasulupanasabotla@gmail.com'])
        msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        mail.send(msg)
        
        flash('Message sent successfully!', 'success')
        return redirect(url_for('index'))  # Redirect to homepage after success
    return redirect(url_for('index'))

@app.route('/test-favicon')
def test_favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

if __name__ == '__main__':
    app.run(debug=True)