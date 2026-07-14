#  User role controlled by request parameter

## Vulnerability
* Application trusts client supplied parameter (admin=false) to give adminstration control

## Sub type
* Broken vertical access control via parameter tampering

## Broken assumption
* The developer never thought about manual changing of admin access from false to true

## How did I discover it?
* Reviewed source for account update requests; found an admin-role parameter not exposed in the UI.

## Why did the exploit succeed?
* The exploit succeeded because the server did not verify whether the request to give the admin access to user came from server side or client side

## What is the impact?
* Unauthorized users can access administrative functionality
* An attacker may perform privileged actions such as deleting users or modifying application settings

## Mitigation 
* Never trust client-supplied role/permission fields
* Use server side authorization for every admin request
