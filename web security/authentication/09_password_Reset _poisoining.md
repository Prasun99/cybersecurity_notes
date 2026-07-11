# Password Reset Poisoning

## Vulnerability

The application generates password reset links using the user-controlled **Host** header instead of a trusted server-side domain. This allows an attacker to manipulate the password reset URL sent to the victim.



---

## How the Attack Works

1. The attacker initiates a password reset request for the victim's account
2. Before sending the request, the attacker modifies the host header to redirect to a domain they control
3. The application generates the password reset link using this host
4. The victim receives the email and clicks the reset link
5. The password reset token is sent to the attacker's server
6. The attacker captures the token and uses it to reset the victim's password

### X-Forwarded-Host
* It is a http header which can trick the server to send or generated different URL than it intended 

---

## Mitigation

- Never trust user-controlled headers such as  `X-Forwarded-Host` when generating URLs.
- Generate password reset links using a trusted server-side configured domain.
- Use cryptographically secure, single-use, short-lived reset tokens.
- Expire reset tokens immediately after use.

---

### Key Takeaway

Applications should never rely on client-supplied HTTP headers to construct sensitive URLs. Password reset links must always be generated using a trusted server-side configuration to prevent attackers from stealing reset tokens.