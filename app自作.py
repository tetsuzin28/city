from flask import Flask,request,render_template,session,redirect,url_for
import os

#インスタンス生成
app= Flask(__name__)

key=os.urandom(21)
app.secret_key=key

id_pwd={'lelouch': 'vermillion'}

#メイン
@app.route('/')
def index():
        if not session.get('login'):
            return redirect(url_for('login'))
        else:
            return render_template('index.html')

@app.route('/login')
def login():
        return render_template ('login.html')

#ログインの認証
@app.route('/logincheck',methods=['POST'])
def logincheck():
    user_id=request.form['user_id']
    password = request.form['password']

    if user_id in id_pwd:
        if password == id_pwd[user_id]:
            session['login'] = True
        else:
            session['login']=False
    else:
        session['login'] =False


    if  session['login']:
        return  redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

#ログアウト
@app.route('/logout')
def logout():
    session.pop('login',None)
    return  redirect(url_for('index'))

@app.route('/pref_quiz',method=[POST])
def pref_quiz():


#アプリケーションの起動
if __name__== '__main__':
    app.run(debug=True)












#アプリケーションの起動
if __name__=='__main__':
    app.run(debug=True)

