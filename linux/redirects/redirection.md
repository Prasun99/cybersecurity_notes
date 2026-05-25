# Redirections in Linux

---

## Uses of Redirection
- Save command output into files
- Combine outputs from multiple commands
- Store logs and results
- Separate errors from normal output

---

## File Descriptors

A file descriptor is a number that represents an open file in Linux.

---

## Standard Output (stdout-1)

### 1. Overwrite output (`>`)

```bash
ls > file.txt
```

- Saves output of command into file
- Overwrites existing content

Example:

```bash
echo "hello" > file.txt
cat file.txt
```

---

### 2. Append output (`>>`)

```bash
ls >> file.txt
```

- Adds output to existing file
- Does NOT delete old data

Example:

```bash
echo "buddy" >> file.txt
cat file.txt
```

---

## Standard Input (stdin-0)

```bash
command < file.txt
```

- Takes input from a file instead of keyboard

---

## Standard Error (stderr)

```bash
command 2> error.txt
```

- Saves error messages into a file

Example:

```bash
ls wrongfile 2> error.txt
```

---

## What I Learned
- How redirection works in Linux
- Difference between > and >>
- Basics of file descriptors