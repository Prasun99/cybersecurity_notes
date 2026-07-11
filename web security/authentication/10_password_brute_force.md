# Password cracking using brute force


## Vulnerability

The password change functionality applies brute-force protection inconsistently. When a user submits the correct current password but provides mismatched values in the two "new password" fields, the request bypasses the mechanism that would normally trigger a lockout or soft timeout after repeated failed password verification attempts.

As a result, an attacker can repeatedly submit password change requests with different guesses for the current password while intentionally supplying mismatched new passwords, avoiding the application's brute-force protection.

---

## Exploitation

1. Authenticate to the application using a valid account
2. Intercept the password change request with an HTTP proxy 
3. Modify the request so that the two new password fields contain different values
4. Because mismatched new passwords bypass the brute-force protection, the attacker can continue guessing the current password without triggering the usual soft timeout or lockout.
5. Once the correct current password is identified, submit a final request with matching new password fields to successfully change the account password.

---

## Mitigation 
* Keep the brute force protection consistent
* Dont display "current password is incorrect" 
* Log and monitor repeated failed password change requests to detect brute-force activity.