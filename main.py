from flask import Flask

app = Flask(__name__)

flask_app_path = app.root_path

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        # Display the contact form
        return render_template('contact.html')
    elif request.method == 'POST':
        # Validate and process the contact form
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Send an email with the contact form data
        send_email(name, email, message)

        # Display a success message
        return render_template('contact_success.html')



@app.route('/', methods=['GET'])
def index():
    # ...

    return render_template('index.html', contact_link=url_for('contact'))


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
