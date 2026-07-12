# Broken brute-force protection

## Vulnerability 
The brute force protection can be bypassed using array of password. The application processes each password in array as a single login request allowing an attacker to test many passwords while avoiding the normal rate limits or temporary lockouts

## How hackers exploit it 
1. Using intercepting proxy they capture the login request 
2. Modify multiple password in array to send it a a single login request using repeater
3. Once a correct password is found, the application returns a valid session ID. The attacker copies this session ID and inserts it into the browser's session cookie to gain authenticated access to the application


## Mitigation 
* Different sesssion code should be provided for each log in 
* Accept single password for a login request
* Session ID should have time out 
* Better brute force protection should be implemented