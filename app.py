from flask import Flask,render_template

app = Flask(__name__)

#Home
@app.route('/')
def home():
    return render_template('home.html')

#About
@app.route('/about')
def about():
    return  render_template('about.html')

#Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

#Username
@app.route('/<username>')
def show_user(username):
    return render_template('user.html')

#Form handling
from flask import Flask, render_template, request
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return render_template('submit.html', name=name, email=email)
    return render_template('submit_form.html')

#Method handling
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # Handle POST request
        name = request.form.get('name')
        email = request.form.get('email')
        return render_template('submit.html', name=name, email=email)
    else:
        # Handle GET request
        default_name = "Esther"
        return render_template('submit_form.html', default_name=default_name)
    

# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Route that redirects to another route after a certain delay
@app.route('/redirect_with_delay')
def redirect_with_delay():
    # Add a delay of 5 seconds (you can adjust the delay as needed)
    time.sleep(5)
    return redirect(url_for('redirected_route'))

# The route to which you want to redirect
@app.route('/redirected_route')
def redirected_route():
    return render_template('redirected.html')


if __name__ == '__main__':
    app.run(debug=True)




