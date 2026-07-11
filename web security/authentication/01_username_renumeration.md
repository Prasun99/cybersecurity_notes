# Username Enumeration via Different Responses

## Objective

Understand how an application can unintentionally reveal whether a username exists by returning different responses during the login process.

---

## Vulnerability

The application returns different responses for:

* An invalid username
* A valid username with an incorrect password

This difference acts as an **oracle**.

> **Oracle:** Any place where two internal code paths produce different observable outputs, allowing an attacker to infer information about the application's internal state.

Because the application behaves differently depending on whether a username exists, an attacker can enumerate valid accounts before attempting to guess passwords.

---

## Key Concepts

### Username Enumeration

Username enumeration is the process of discovering valid usernames by observing differences in the application's responses.

Possible indicators include:

* Response length
* Status code
* Response body
* Response timing
* Redirect behavior
* Cookies

---

### Why the Response Length Changes

When a **valid username** is submitted:

1. The application finds the account.
2. It proceeds to password verification (or password hash verification).
3. It generates a response indicating that authentication failed because of an incorrect password.

When an **invalid username** is submitted:

1. The application immediately rejects the request.
2. Password verification is skipped.

Since these requests follow different internal code paths, the responses may differ in length, content, or timing.

> **Note:** Response length is only one possible indicator. Other applications may leak information through different observable behaviors.

---

### Password Testing

After identifying a valid username:

* Keep the username fixed.
* Test candidate passwords.

A successful login usually produces a different server response, such as:

* A redirect 
* A different page
* A new session cookie
* Different response content

The important observation is that the application behaves differently after successful authentication.

---

## Burp Suite – Intruder

**Burp Intruder** automates repetitive HTTP requests.

It replaces a chosen parameter (such as a username or password) with values from a payload list and sends each request automatically, making large-scale testing significantly faster than manual requests.

---

## Impact

If username enumeration is possible, an attacker can:

* Discover valid user accounts.
* Reduce the search space for password attacks.
* Make brute-force and credential stuffing attacks more effective.
* Gather information about the application's users.

---

## Mitigations

Developers can reduce this risk by:

* Returning the same generic error message for both invalid usernames and incorrect passwords.
* Keeping responses consistent in content, length, timing, and status codes where practical.
* Implementing rate limiting and account lockout mechanisms.
* Using multi-factor authentication (MFA).
* Monitoring and logging repeated authentication failures.

---

## Key Takeaways

* Authentication should not reveal whether a username exists.
* Small differences in server responses can leak sensitive information.
* Enumeration is often the first step before password attacks.
* Burp Intruder is useful for automating repetitive authentication testing.
