from models import account
def check_login(username, password):
    return account.check_account_credentials(username,password)

def check_account(username):
    return account.account_exists(username)

def check_register(username,password,confirmPassword):
    if password != confirmPassword:
        return False
    elif account.account_exists(username):
        return False
    return True
