import json

def save_email_to_local_storage(email):
    try:
        with open('emails.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    data['email_user'] = email

    with open('emails.json', 'w') as file:
        json.dump(data, file)
def get_email_from_local_storage():
    try:
        with open('emails.json', 'r') as file:
            data = json.load(file)
            email = data.get('email_user', None)
    except FileNotFoundError:
        email = None
    return email
def share_email(email):
    save_email_to_local_storage(email)
    return email
def another_method():
    email_user = get_email_from_local_storage()
    print(email_user)
    return email_user


