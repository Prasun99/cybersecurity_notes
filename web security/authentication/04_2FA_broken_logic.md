# 2FA Broken Logic (Authentication Vulnerabilities)

## Vulnerability 



* **Broken Authentication / Flawed Business Logic**

  * The application assumes that the client-supplied `verify` cookie identifies the user currently completing the authentication process.
  * Instead of validating the user's identity through a secure server-side session, it trusts client-controlled input.

* **Insecure Session Management**

  * The 2FA process is not securely linked to a successful username/password authentication.
  * Any client capable of modifying the `verify` cookie can attempt to complete 2FA for another user.

* **Missing Rate Limiting / Brute-Force Protection**

  * The application accepts unlimited 4 digit authentication attempts.
  * There are no account lockouts or token invalidation after repeated failures, making brute-force attacks practical.

---

# How hacker exploits it 
- Initiate the normal login process using any valid account credentials.
- Observe that after the first login step, the application sends a GET /login2 request to generate a 4-digit 2FA code.
- Identify that the application uses the client-controlled verify cookie to determine which user's 2FA code should be validated.
- Modify the verify cookie to the target username
- This causes the server to generate a fresh 2FA code for the target account without verifying the password.
- Keep the modified verify=carlos cookie and send the request to Burp Intruder.
- Configure the 2FA code parameter as the payload position and brute-force all values from 0000 to 9999.
- Monitor the responses for a successful login (change in status code)
- Once the correct code is discovered, the server creates a valid authenticated session for the target user.

---

# Root Cause

The application incorrectly trusts a client-controlled cookie to identify the user undergoing 2FA.

The authentication flow is not bound to a secure server-side session, allowing the attacker to manipulate the authentication state by modifying client-side data.

---

# Security Impact

* Password authentication can be bypassed.
* Unauthorized users can attempt MFA verification for any account.
* Unlimited brute-force attempts make guessing the 2FA code feasible.
* Successful exploitation results in full account takeover.

---
###  Mitigation Strategies

* Store the authentication state on the server, never in client-controlled cookies, and require successful password verification before allowing access to the 2FA endpoint.
* Implement brute-force protections by rate limiting requests, locking accounts after multiple failed attempts, invalidating 2FA codes after a few failures


