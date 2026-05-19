# What I Did Today

- Understood permissions in Linux
- Practiced changing permissions and ownership for files and directories

---

# Understanding Permissions

Linux permissions have three types:

- Read (`r`)
- Write (`w`)
- Execute (`x`)

Example:
```bash
-rwxr--r--
```

First character meaning:
```bash
- -> file
d -> directory
```

Permission groups:
```bash
rwx | r-- | r--
user  group others
```

---

# Changing Permissions Using chmod

The `chmod` command is used to change permissions for files and directories.

There are two methods:
- Symbolic Method
- Octal Method

## Symbolic Method

Symbols:
```bash
u -> user(owner)
g -> group
o -> others
a -> all
```

Operators:
```bash
+ -> add permission
- -> remove permission
= -> set exact permission
```

Permission symbols:
```bash
r -> read
w -> write
x -> execute
```

Examples:
```bash
chmod go=rwx test1.txt
chmod go-wx test1.txt
```

---

## Octal Method

Permission number values:
```bash
4 -> read
2 -> write
1 -> execute
```

Examples:
```bash
7 = 4+2+1 = rwx
6 = 4+2   = rw-
5 = 4+1   = r-x
4 = read only
```

Commands:
```bash
chmod 444 test1.txt
chmod 744 test1.txt
```

---

# Important Commands Practiced

```bash
ls -alh
chmod go=rwx test1.txt
chmod go-wx test1.txt
chmod 444 test1.txt
chmod 744 test1.txt
```
# File and Directory Ownership

```bash
chown -> changes the owner of a file or directory
chgrp -> changes the group of a file or directory
```