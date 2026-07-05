# 2FA Authentication Bypass

## Objective

Bypass the two-factor authentication (2FA) process without providing a valid 2FA verification code.

---

## Vulnerability

The application creates a valid authenticated session immediately after verifying the username and password, before the user completes 2FA.

Using Burp Suite, an attacker can intercept and manipulate the authentication flow 

---

## Key Concepts

### Authentication Flow

A secure authentication flow should follow this sequence:

1. User submits a valid username and password.
2. Server requests a valid 2FA code.
3. Server verifies the 2FA code.
4. Only then is the user granted full access to protected resources.

In this vulnerable application, the session is created too early, allowing access to protected pages without successfully completing step 3.

---

### HTTP Request

An HTTP request is a message sent from the browser to the server requesting an action, such as logging in, loading a page, or submitting a 2FA code with no encryption.

---



### Burp Suite – Intercept

Intercept pauses HTTP requests before they reach the server.

It allows you to:

* View the request.
* Modify the request.
* Forward the request to the server.
* Drop the request so it never reaches the server.

Intercept is used to observe and control live browser traffic during security testing.

---

### Drop

Dropping a request discards it completely instead of forwarding it to the server. This interrupts the normal authentication flow. Here only droping doesnt cause the bypass changing the url to ***myaccount*** does(which can be received from http history ). Since application already created a valid season without validating the 2FA it bypasses it completely
---


### Repeater

Repeater creates a copy of an HTTP request that can be resent and modified multiple times without using the browser again.

It is useful for:

* Inspecting requests and responses.
* Testing different parameters.
* Replaying authentication requests.
* Understanding how the server validates user input.

---

## Key Learning Points

* Authentication and 2FA are separate stages of the login process.
* A session should not be fully authenticated until 2FA has been successfully verified.
* Intercepting or dropping HTTP requests does not create the vulnerability—it only helps reveal it.
* Authentication bypass vulnerabilities are caused by incorrect server-side validation, not by the client or the testing tool.
* Always analyze when the session is created and what checks the server performs before granting access to protected resources.


#### Basic workflow
1 Logs in using uid and pw (session is already created)
2 requests 4 digit code (can be bypassed)
3 my account page is opened