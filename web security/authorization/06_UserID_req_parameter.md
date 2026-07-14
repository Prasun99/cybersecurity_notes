# User ID Controlled by Request Parameter (IDOR)

## Vulnerability
Application trusts a client-supplied id parameter ( `id=carlos` grants access to 
carlos's account) with no server-side ownership check.

## Sub-type
Broken horizontal access control via parameter tampering (IDOR). Horizontal because the 
attacker gains access to another user's data at the same privilege level — no privilege 
escalation involved, unlike the `roleid`/`admin` cases

## Broken assumption
 Developer assumed users would never manually modify or enumerate id to access other user's account

## Discovery
Reviewed source for account/profile requests; found an id field present in the request 
but not explained or restricted in the UI

## Why the exploit succeeded
The server used the client-supplied id directly to fetch the target record, 
without checking that id matched the authenticated session's own user ID. Object lookup 
was never scoped to the requester — any authenticated user could reference any other 
user's object.

## Impact
- Any authenticated user can access or modify another user's account/data
- Attacker may extract sensitive information without needing that user's credentials

## Mitigation
- Never trust a client-supplied object/user ID for authorization decisions
- Use indirect references instead of predictable/enumerable IDs where feasible