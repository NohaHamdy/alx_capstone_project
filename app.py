from flask import Flask, render_template , url_for, request
import smtplib

app = Flask(__name__)

flask_app_path = app.root_path
app.static_folder = 'templates'

@app.route('/contact', methods=['GET', 'POST'])



def contact():
    if request.method == 'GET':
        # Display the contact form
        return render_template('contact_form.html')
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


def send_email(name, email, message):
    email_server = smtplib.SMTP('smtp.gmail.com', 587)
    email_server.starttls()
    email_server.login('nohatota99@gmail.com', '######')

    email_message = """
From: {} <{}>
To: {}
Subject: Contact form submission

{}
""".format(name, email, 'nohatota99@gmail.com', message)

    email_server.sendmail('nohatota99@gmail.com', 'nohatota99@gmail.com', email_message)
    email_server.quit()



if __name__ == '__main__':
    app.run(debug=True)

