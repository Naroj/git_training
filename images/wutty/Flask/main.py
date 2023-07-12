from flask import Flask, render_template, redirect, request, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.validators import DataRequired, URL
from werkzeug import exceptions
import os, crypt, requests, time, string

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
GITEA_URL = "http://gitea:3000/api/v1"
GITEA_TOKEN = os.getenv('GITEA_TOKEN')


class CafeForm(FlaskForm):
    naam = StringField('Naam', validators=[DataRequired()])
    wachtwoord = StringField('Wachtwoord', validators=[DataRequired()])
    submit = SubmitField('Submit')

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    # allow alphanumeric
    allow = tuple(tuple(str(i) for i in range(0, 10)) + tuple(string.ascii_lowercase))
    if form.validate_on_submit():
        for char in list(form.naam.data):
            try:
                allow.index(char)
            except ValueError as err:
                raise exceptions.BadRequest(
                  f"failed to add user, it contains unexpected characters, choose only alphabetic characters"
                )

        res = adduser(form.naam.data, form.wachtwoord.data)
        if res[0] == 0:
            add_git_user(form.naam.data, form.wachtwoord.data)
            add_git_pubkey(form.naam.data, res[1])
            return render_template('cafes.html', form=form)
        else:
            raise exceptions.BadRequest(f"failed to add system user: {form.naam.data}")
    else:
        for err in form.errors:
            print(f"error: {err}")
    return render_template('add.html', form=form)

def adduser(user, pw):
    us = os.system(f"adduser {user} -D")
    pw = os.system(f"echo '{user}:{pw}' | chpasswd")
    ssh_known_hosts = f"/home/{user}/.ssh/known_hosts"
    set_git_mail = os.system(f"git config --global user.email '{user}@example.nl'")
    set_git_name = os.system(f"git config --global user.name '{user}'")
    mkssh = os.system(f'su {user} -c "ssh-keygen -f /home/{user}/.ssh/id_rsa -P \'""\' "')
    fetch_gitea_keys = os.system(f"ssh-keyscan gitea > {ssh_known_hosts}")
    ssh_perms = os.system(f"chmod 700 {ssh_known_hosts} && chown {user}: {ssh_known_hosts}")
    pubkey = ""
    with open(f"/home/{user}/.ssh/id_rsa.pub", "r") as fp:
        pubkey = fp.read()
    res = us + pw + mkssh
    return res, pubkey

def add_git_user(user, pw):
    endpoint = f"{GITEA_URL}/admin/users?access_token={GITEA_TOKEN}"
    payload = {
        'password': pw, 
        'full_name': user, 
        'Username': user, 
        'email': f'{user}@example.nl', 
        'source_id': 0, 
        'login_name': user, 
        'send_notify': False
    }
    api_call = requests.post(endpoint, json=payload)
    print(f"create_user: {str(api_call)}")

def add_git_pubkey(user, pubkey):
    if not pubkey:
        return
    endpoint = f"{GITEA_URL}/admin/users/{user}/keys?access_token={GITEA_TOKEN}"
    payload = {"key": pubkey, "read_only": False, "title": "default_pubkey"}
    api_call = requests.post(endpoint, json=payload)
    print(f"postpubkey: {api_call}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
