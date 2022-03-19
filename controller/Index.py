from flask import render_template

class Index:

    def get():
        return render_template('index.html'), 200