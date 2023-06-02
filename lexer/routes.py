from lexer import app
from flask import render_template
from .forms import CodeForm, TreeForm

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/lexer', methods=['GET', 'POST'])
def lexer():
    form = CodeForm()
    #if form.validate_on_submit():
        #code = form.Code.data
        # Function Call For Lexical and Syntax Analyzer
     
    return render_template('lexer.html', form=form)


@app.route('/tree', methods=['GET', 'POST'])
def tree():
    form = TreeForm()
    #if form.validate_on_submit():
        #code = form.Code.data
        # Function Call For Lexical and Syntax Analyzer
        
    return render_template('tree.html', form=form)