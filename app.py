from flask import Flask, render_template

def create_app():
    """
    Create yeh Flask app instance
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    return app

app = create_app()

# Dictionary to store error messages
error_messages = {
    404: "Page not found"
}

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(error):

    return render_template('error', error_message=error_messages[404]), 404

if __name__ == '__main__':
    app.run(debug=True)