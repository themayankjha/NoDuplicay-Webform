from flask import Flask, render_template, redirect, url_for, request, g,json,session
from functions import generaterandomid,writeout

app = Flask(__name__)
app.secret_key = "l693RIniKGLM9KPIDHqC5rllJRgg2LA3"


@app.route('/', methods=['GET', 'POST'])
def form():
    uidexists=False
    try:
        json.loads(session['uid'])
        uidexists=True
    except:
        pass
    if uidexists==True:
        return redirect(url_for('alreadydone'))
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone= request.form['phone']
        message= request.form['message']
        randomid=generaterandomid()
        writeout(randomid, name, email, phone, message)
        session['uid']=json.dumps({"uid":randomid,"name":name})
        return render_template('message.html',message="Thank You "+name+"!")
    return render_template('form.html')

@app.route('/alreadydone', methods=['GET', 'POST'])
def alreadydone():
    uid=json.loads(session['uid'])
    name=uid['name']
    message="Hi "+name+" ,You have submitted this form before, Thank you!"
    return render_template('message.html', message=message)