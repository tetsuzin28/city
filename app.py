from flask import Flask, render_template, session, request, redirect, url_for
import os
from pref_question import pref_location #pref_question.pyモジュール

app = Flask(__name__)

key = os.urandom(21)
app.secret_key = key

id_pwd = {'lelouch': 'vermillion'}

@app.route('/')
def index():
    if not session.get('login'):
        return redirect(url_for('login'))
    else:
        return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logincheck', methods=['POST'])
def logincheck():
    user_id = request.form['user_id']
    password = request.form['password']

    if user_id in id_pwd:
        if password == id_pwd[user_id]:
            session['login'] = True
        else:
            session['login'] = False
    else:
        session['login'] = False

    if session['login']:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('index'))

@app.route('/pref_quiz', methods=['POST'])
def pref_quiz():
    random_pref, city_name, pref_url = pref_location()#pref_question.py
    session['prefecture'] = random_pref
    session['city'] = city_name
    session['url'] = pref_url
    return render_template('quiz.html', prefecture=random_pref)

@app.route('/answercheck', methods=['POST'])
def answercheck():
    user_answer = request.form['city']
    prefecture = session.get('prefecture')
    city = session.get('city')
    url = session.get('url')

    if user_answer == city:
        result = '正解！！'
    else:
        result = '残念！！'

    return render_template('result.html', result=result,prefecture=prefecture, city=city, url=url)

if __name__ == '__main__':
    app.run(debug=True)