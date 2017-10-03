from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/validate", methods=['post'])
def validate():
    username = request.form['username']
    password = request.form['password']
    passwordCheck = request.form['passwordVerify']
    email = request.form['email']

    validUsernameBool = True
    validPasswordBool = True
    validVerifyBool = True
    validEmailBool = True

    if username == "" or not validInputString(username):
        validUsernameBool = False

    if password == "" or not validInputString(password):
        validPasswordBool = False
    
    if passwordCheck != password and passwordCheck != "":
        validVerifyBool = False

    if not validEmail(email) and email != "":
        validEmailBool = False

    if not validUsernameBool or not validPasswordBool or not validVerifyBool or not validEmailBool:
        return render_template("baseForm.html", validUsername = validUsernameBool, username = username, validPassword = validPasswordBool, validVerify = validVerifyBool, email=email, validEmail = validEmailBool)
    else:
        return render_template("welcome.html", username = username)

@app.route('/')
def index():
    return render_template('baseForm.html')

#This function checks validity for both the password and the username
def validInputString(inputString):
    stringLength = len(inputString)

    validStringBool = True

    if stringLength < 3 or stringLength > 20:
        validStringBool = False
    elif ' ' in inputString:
        validStringBool = False

    return validStringBool

def validEmail(inputEmail):
    validEmailBool = True

    if '@' not in inputEmail or '.' not in inputEmail or not validInputString(inputEmail):
        validEmailBool = False

    return validEmailBool

app.run()