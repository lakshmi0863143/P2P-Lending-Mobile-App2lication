import anvil.server


@anvil.server.callable
def share_email(email):
    # Save the email directly as a global variable
    globals()['email_user'] = email
    return email


@anvil.server.callable
def another_method():
    # Retrieve the email directly from the global variable
    email_user = globals().get('email_user', None)
    print(email_user)
    return email_user
