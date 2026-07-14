# User Role Modification via `roleid` Parameter

## Vulnerability
Application trusts a client-supplied roleid parameter ( `roleid=2` grants admin) 
to determine authorization level, with no server-side validation

## Sub-type
Broken vertical access control via parameter tampering (enumerable value tampering )
Here attacker doesn't need to know the parameter's purpose, only needs to brute-force 
small integer values until one grants elevated access

## Broken assumption
Developer assumed users would never manually modify or enumerate roleid, and did not 
anticipate brute-forcing of small integer role identifiers.

## Discovery
Reviewed source for account/profile update requests; found a roleid field present in 
the request body but not exposed or explained in the UI.

## Why the exploit succeeded
The application failed to enforce server-side authorization and did not restrict which fields a regular user was permitted to modify, allowing privilege escalation through parameter tampering

## Impact
- Unauthorized users can gain administrative privileges
- Attacker may perform privileged actions (delete users, modify application settings)

## Mitigation
- Never trust client-supplied role/permission fields
- Enforce server-side authorization for every privileged field, not just privileged endpoints
- Use random token or id for each users
- Re-validate the requester's authority on the specific field being changed, not just that they're authenticated

## Residual risk
Stripping roleid from the profile-update endpoint doesn't guarantee safety — if another 
endpoint writes to the same DB field (e.g. a bulk-import or internal API), the same 
vulnerability can resurface through a different path. Privilege-granting actions should 
be centrally logged and gated, not just filtered per-endpoint.