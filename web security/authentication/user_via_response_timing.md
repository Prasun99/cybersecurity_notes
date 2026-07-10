

# Vulnerability 
The application provides different response time for valid and invalid username:
* Invalid username: The application quickly rejects the request.
* Valid username: The application continues to verify the password, which takes longer.  



# How can hacker exploit this lab 
1. Firstly they check the response time of the application,for valid username it is higher since it reaches to password verification step 
2. Next they check if the application accepts the x forwaded for provided by client which tackles the limited access problem 
3. Then they use pitchfork attack to assign different ip to each username and password compare response time then brute force the password to access the lab 


## Reverse proxy 
It is a server sided software which is used to hide the backends ip address improves performance using caching. It solves the problem of unlimited tries to access the account if the proxy is configurated to do so,as we faced in  previous user enumeration lab. 

## X forwaded for 
It is a header which tells the application who the real user is 

### How is it a vulnerability 
If the application trusts X-Forwarded-For when it shouldn't, an attacker may be able to influence how the application identifies the client.


## Pitch fork attack
A Pitchfork attack is a password attack technique where multiple usernames are paired with multiple passwords in parallel, instead of trying every password against every username.
In this lab this attack is used since there is limit to access the account and each username and password uses different x forwaded to ip address to exploit the vulnerability 

## How to fix this vulnerability
The application should  only Trust X-Forwarded-For only from trusted proxies
Rate-limit per account as well as per IP