# User Enumeration via Different Responses

## Goal

 Enumerate a valid username and Brute-force the password for that username.

## Concept

This lab is similar to Lab 1. It solves the vulnerability of lab 1. It has different response length for both vaild and invalid username .

## Vulnerability

Invalid username or password has **Invalid username or password** in their html code which can exploites using filter tool 

## Exploitation

1. Send login requests using a list of incorrect usernames and password.
2. Use Burp Suite Intruder to automate the requests.
3. Compare the responses (using response content, filtering, or response length) to identify the username whose response differs from the others.
4. After identifying the valid username, perform a password brute-force attack against that account using a password wordlist.
5. Log in with the discovered credentials to complete the lab.

## Mitigation
1. Devlopers can use captca to avoid brute force attack
2. Use a boolean flag to track failure, and render the exact same error page
