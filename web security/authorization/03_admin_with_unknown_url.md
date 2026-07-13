# Unprotected admin functionality with unpredictable URL

## Vulnerability
* Lack of enforcement of access control on admin endpoint

## Broken assumption
* The developer relied on the secrecy of the URL instead of enforcing server-side access control.

## How did I discover it?
* By reviewing the source code the hidden URL for admin panel was revealed

## Why did the exploit succeed?
* The exploit succeeded because the server did not verify whether the requester was authorized to access the admin endpoint. Knowing the hidden URL was enough to gain access

## What is the impact?
* Unauthorized users can access administrative functionality
* An attacker may perform privileged actions such as deleting users or modifying application settings

## Mitigation 
* Never rely on unpredicatable or hidden URLs
* Use server side authorization for every admin request
