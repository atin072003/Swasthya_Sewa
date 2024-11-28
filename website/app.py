from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used to secure session data

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle contact form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Process form data (in a real app, save to a database or send an email)
    flash(f'Thank you, {name}! We have received your message.')

    # Redirect back to the home page
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
