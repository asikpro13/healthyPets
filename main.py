from flask import Flask, render_template, send_from_directory, url_for
import os


application = Flask(__name__)


@application.route('/')
def main():
    return render_template('main.html')


@application.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(application.root_path, 'static'),
                          'favicon.png', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5001, debug=True)