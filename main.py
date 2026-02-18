from pyscript import display, document

def signing_up(e):
    document.getElementById('output').innerHTML = ' '

    user = document.getElementById('username').value
    password = document.getElementById('password').value

    user_length = len(user)
    pass_length = len(password)

    if user_length < 7:
        display(f'Your username must be atleast seven characters', target='output')
    
    if pass_length < 10:
        display(f'Your password must be atleast 10 characters', target='output')
    elif not any(char.isalpha() for char in password):
        display('Password must have at least 1 letter', target='output')
    elif not any(char.isdigit() for char in password):
        display('Password must have at least 1 number', target='output')
    else:
        display(f'You are now signed in!', target='output')

def team_identity(e):
    document.getElementById('result').innerHTML =  '    '
    reg = document.getElementById('reg').value
    cert = document.getElementById('cert').value
    grade = document.getElementById('grade').value
    section = document.getElementById('section').value
    
    if reg == "Yes" and cert == "Yes" and grade == "7" and section == "eme":
        display(f'Congrats, you are blue bears 🐻', target='result')

    elif reg == "Yes" and cert == "No" and grade == "7" and section == "eme":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "7" and section == "eme":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "7" and section == "eme":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "8" and section == "eme":
        display(f'Congrats, you are blue bears 🐻', target='result')

    elif reg == "Yes" and cert == "No" and grade == "8" and section == "eme":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "8" and section == "eme":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "8" and section == "eme":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "9" and section == "eme":
        display(f'Congrats, you are blue bears 🐻', target='result')

    elif reg == "Yes" and cert == "No" and grade == "9" and section == "eme":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "9" and section == "eme":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "9" and section == "eme":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "10" and section == "eme":
        display(f'Congrats, you are yellow tigers 🐯', target='result')

    elif reg == "Yes" and cert == "No" and grade == "10" and section == "eme":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "10" and section == "eme":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "10" and section == "eme":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "7" and section == "ruby":
        display(f'Congrats, you are red bulldogs 🐶', target='result')

    elif reg == "Yes" and cert == "No" and grade == "7" and section == "ruby":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "7" and section == "ruby":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "7" and section == "ruby":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "8" and section == "ruby":
        display(f'Congrats, you are blue bears 🐻', target='result')

    elif reg == "Yes" and cert == "No" and grade == "8" and section == "ruby":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "8" and section == "ruby":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "8" and section == "ruby":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "9" and section == "ruby":
        display(f'Congrats, you are red bulldogs 🐶', target='result')

    elif reg == "Yes" and cert == "No" and grade == "9" and section == "ruby":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "9" and section == "ruby":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "9" and section == "ruby":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "10" and section == "ruby":
        display(f'Congrats, you are blue bears 🐻', target='result')

    elif reg == "Yes" and cert == "No" and grade == "10" and section == "ruby":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "10" and section == "ruby":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "10" and section == "ruby":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "7" and section == "sapph":
        display(f'Congrats, you are green hornets 🐝', target='result')

    elif reg == "Yes" and cert == "No" and grade == "7" and section == "sapph":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "7" and section == "sapph":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "7" and section == "sapph":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "8" and section == "sapph":
        display(f'Congrats, you are yellow tigers 🐯', target='result')

    elif reg == "Yes" and cert == "No" and grade == "8" and section == "sapph":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "8" and section == "sapph":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "8" and section == "sapph":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "9" and section == "sapph":
        display(f'Congrats, you are green hornets 🐝', target='result')

    elif reg == "Yes" and cert == "No" and grade == "9" and section == "sapph":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "9" and section == "sapph":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "9" and section == "sapph":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "10" and section == "sapph":
        display(f'Congrats, you are green hornets 🐝', target='result')

    elif reg == "Yes" and cert == "No" and grade == "10" and section == "sapph":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "10" and section == "sapph":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "10" and section == "sapph":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "7" and section == "top":
        display(f'Congrats, you are yellow tigers 🐯', target='result')

    elif reg == "Yes" and cert == "No" and grade == "7" and section == "top":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "7" and section == "top":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "7" and section == "top":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "8" and section == "top":
        display(f'Congrats, you are green hornets 🐝', target='result')

    elif reg == "Yes" and cert == "No" and grade == "8" and section == "top":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "8" and section == "top":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "8" and section == "top":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "9" and section == "top":
        display(f'Congrats, you are yellow tigers 🐯', target='result')

    elif reg == "Yes" and cert == "No" and grade == "9" and section == "top":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "9" and section == "top":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "9" and section == "top":
        display(f'Not eligible', target='result')

    elif reg == "Yes" and cert == "Yes" and grade == "10" and section == "top":
        display(f'Congrats, you are red bulldogs 🐶', target='result')

    elif reg == "Yes" and cert == "No" and grade == "10" and section == "top":
        display(f'Needs medical certificate', target='result')

    elif reg == "No" and cert == "Yes" and grade == "10" and section == "top":
        display(f'Please register online', target='result')

    elif reg == "No" and cert == "No" and grade == "10" and section == "top":
        display(f'Not eligible', target='result')

    else:
        display(f'Please fill out all forms', target='result')