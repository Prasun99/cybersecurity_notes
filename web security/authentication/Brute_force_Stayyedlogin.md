# Brute-Forcing a Stay-Logged-In Cookie

## Vulnerabilities
* Weak cookie design (consists of username and hashed password)
* Missing brute force protection
* The application trusts the stay-logged-in cookie as proof of authentication, allowing login without entering credentials

---

## How the hackers exploit it
1. Firstly they login using valid credentials and trace the http requests 
2. Decode the login cookie to figure out its format 
3. Using burp suite's intruder and monitor response for successful access 

## How to prevent this 
* Use brute force prevention 
* Use long, cryptographically random remember-me tokens 
* Use different and unique cookie for each session

---

### Tool (Payload processing)
* MD5 is used to hash the password into the format expected by the application.
* Add Prefix  is used to construct the cookie in the required username:md5(password) format.
* Base64 is used to encode the entire cookie value into a safe, printable format for transmission and storage in an HTTP cookie.
* The processing must occur in this order because each step depends on the output of the previous one, matching how the application generates and validates the cookie.