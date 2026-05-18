
# What I did today
Started learning basic Linux commands on WSL Ubuntu.
Practiced file creation, editing, copying, moving, and deletion.

---

# Commands Practiced

## pwd
Prints current working directory.
```bash
pwd
# Output: /home/prasun
```

## ls
Lists files in current directory.
```bash
ls          # basic list
ls -l       # detailed list
ls -al      # includes hidden files
ls -lR      # recursive listing
```

## touch
Creates an empty file.
```bash
touch test.txt
```

## echo
Prints text or writes to a file.
```bash
echo "i am inevitable"          # prints to terminal
echo "Hello" > test.txt         # writes to file (overwrites)
echo "Hello" >> test.txt        # appends to file
```

## cat
Reads and displays file content.
```bash
cat test.txt                    # display file
cat test.txt > test1.txt        # copy content to new file
```

## cp
Copies a file to a destination.
```bash
cp Test.txt Test/               # copies Test.txt into Test folder
```

## mv
Moves or renames a file.
```bash
mv test.txt Test/               # moves file into folder
mv test.txt test1.txt           # renames file
```

## mkdir
Creates a new directory.
```bash
mkdir Test
```

## rmdir
Removes an empty directory.
```bash
rmdir Test
```

## rm
Removes files or directories.
```bash
rm test1.txt                    # remove a file
rm -R Test/                     # remove directory and its contents
```

## whatis
Gives a one-line description of a command.
```bash
whatis touch    # touch (1) - change file timestamps
whatis echo     # echo (1) - display a line of text
whatis mv       # mv (1) - move (rename) files
whatis nano     # nano (1) - text editor
whatis vim      # vim (1) - Vi IMproved, a programmer's text editor
```

---

# Key Concepts Learned

## Redirection
| Operator | Meaning |
|----------|---------|
| `>` | Write to file (overwrites existing content) |
| `>>` | Append to file (keeps existing content) |

## Hidden Files
Running `ls -al` revealed dotfiles like `.bashrc`, `.profile`, `.bash_history`.
These are configuration files hidden by default (start with `.`).

## Case Sensitivity
Linux is case-sensitive. `ls` works but `LS` does not.
`Test/` and `test.txt` are treated as completely different names.

---



## Reflections
- Linux commands are short but powerful
- Small typos cause big errors — read output carefully
- `whatis` is a great way to quickly understand any command
- `rm -R` is dangerous — it deletes everything permanently

---

