# SUID and SGID 

---

## SUID
- It is a special permission for user 
- It is a command set on file and when the file is executed it will be executed by the owner rather than a user 
- To put it in a simple term when a file with SUID is executed, the process runs with the owner’s permissions (usually root), not the user’s permissions
- SUID applies to executable files only, not normal files
- Denoted by s or S

Command
```bash
chmod u+s file_name
```
-You need root/sudo if you are modifying system-owned files 

---

## SGID
- It is similar to SUID but the file gets executed as group who owns the file
- If set on directory the file will have group ownership 

Command
```bash 
chmod g+s file_name 
```
---

### Security Risk

If misconfigured:
- Can allow privilege escalation attacks
- Attackers may exploit vulnerable SUID binaries

---

## Sticky Bit
- If sticky bit is used in a file or directory then only the owner can delete or rename 
that particular file
- It is important while working in group since others cannot rename or delete the file even if they have execute command
- denoted by t

Command
```bash
chmod o+t file_name
```

--- 

### Other thing i learned 
- sudo -i => changes directory to root 
- su - user_name => to change the user 
