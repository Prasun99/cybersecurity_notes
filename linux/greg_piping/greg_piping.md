# Grep and Piping in Linux


## Grep
``` bash
grep is used to search text or patterns inside files or command output.

Basic syntax:

grep "word" filename

Example:

grep "hello" notes.txt

This searches for the word "hello" inside notes.txt.

Common grep Examples

Case insensitive search
grep -i "hello" notes.txt

Matches:
hello
Hello
HELLO

Show line numbers
grep -n "hello" notes.txt

Search recursively in directories
grep -r "password" .

Searches all files in current directory and subdirectories.

Invert match
grep -v "hello" notes.txt

Shows lines that do NOT contain "hello".
``` 

## Piping
```bash
Pipe symbol   "|"
Piping sends output of one command into another command.

Syntax:
command1 | command2

Meaning:
command1 produces output
command2 uses that output as input
Piping Examples
Example 1
ls -al | grep ".txt"
ls -al lists files
grep ".txt" filters only .txt files

Example 2
history | grep chmod

Shows commands from history containing chmod.
```

## Why Piping is Powerful

- Pipes let you combine small Linux commands together.

