This is about shell redirections and filters

REDIRECTION
(>): used to redirect stndard output
e.g  ls > file_list.txt

(>>): When the results are appended, the new results are added to the end of the file, thus making the file longer each time the command is repeated. If the file does not exist when we attempt to append the redirected output, the file will be created.
e.g ls >> file_list.txt

(<): is used to redirect standard input
e.g  sort < file_list.txt

sort < file_list.txt > sorted_file_list.txt
As we can see, a command can have both its input and output redirected. Be aware that the order of the redirection does not matter. The only requirement is that the redirection operators (the "<" and ">") must appear after the other options and arguments in the command.

COMMAND  used together with pipelines
ls -lt | head: Displays the 10 newest files in the current directory.

du | sort -nr: Displays a list of directories and how much space they consume, sorted from the largest to the smallest.

find . -type f -print | wc -l: Displays the total number of files in the current working directory and all of its subdirectories.

COMMON programs that can act as filters:
sort: Sorts standard input then outputs the sorted result on standard output.

uniq: Given a sorted stream of data from standard input, it removes duplicate lines of data (i.e., it makes sure that every line is unique).

grep: Examines each line of data it receives from standard input and outputs every line that contains a specified pattern of characters.

fmt: Reads text from standard input, then outputs formatted text on standard output.

pr: Takes text input from standard input and splits the data into pages with page breaks, headers and footers in preparation for printing.

head: Outputs the first few lines of its input. Useful for getting the header of a file.

tail: Outputs the last few lines of its input. Useful for things like getting the most recent entries from a log file.

tr: Translates characters. Can be used to perform tasks such as upper/lowercase conversions or changing line termination characters from one type to another (for example, converting DOS text files into Unix style text files).

sed: Stream editor. Can perform more sophisticated text translations than tr.

awk: An entire programming language designed for constructing filters. Extremely powerful.

SPECIAL CHARACTERD USED BY BASH

" "

Whitespace — this is a tab, newline, vertical tab, form feed, carriage return, or space. Bash uses whitespace to determine where words begin and end. The first word is the command name and additional words become arguments to that command.

$

Expansion — introduces various types of expansion: parameter expansion (e.g. $var or ${var}), command substitution (e.g. $(command)), or arithmetic expansion (e.g. $((expression))). More on expansions later.

''

Single quotes — protect the text inside them so that it has a literal meaning. With them, generally any kind of interpretation by Bash is ignored: special characters are passed over and multiple words are prevented from being split.

""

Double quotes — protect the text inside them from being split into multiple words or arguments, yet allow substitutions to occur; the meaning of most other special characters is usually prevented.

\

Escape — (backslash) prevents the next character from being interpreted as a special character. This works outside of quoting, inside double quotes, and generally ignored in single quotes.

#

Comment — the # character begins a commentary that extends to the end of the line. Comments are notes of explanation and are not processed by the shell.

=

Assignment -- assign a value to a variable (e.g. logdir=/var/log/myprog). Whitespace is not allowed on either side of the = character.

[[ ]]

Test — an evaluation of a conditional expression to determine whether it is "true" or "false". Tests are used in Bash to compare strings, check the existence of a file, etc. More of this will be covered later.

!

Negate — used to negate or reverse a test or exit status. For example: ! grep text file; exit $?.

>, >>, <

Redirection — redirect a command's output or input to a file. Redirections will be covered later.

|

Pipe — send the output from one command to the input of another command. This is a method of chaining commands together. Example: echo "Hello beautiful." | grep -o beautiful.

;

Command separator — used to separate multiple commands that are on the same line.

{ }

Inline group — commands inside the curly braces are treated as if they were one command. It is convenient to use these when Bash syntax requires only one command and a function doesn't feel warranted.

( )

Subshell group — similar to the above but where commands within are executed in a subshell (a new process). Used much like a sandbox, if a command causes side effects (like changing variables), it will have no effect on the current shell.

(( ))

Arithmetic expression — with an arithmetic expression, characters such as +, -, *, and / are mathematical operators used for calculations. They can be used for variable assignments like (( a = 1 + 4 )) as well as tests like if (( a < b )). More on this later.

$(( ))

Arithmetic expansion — Comparable to the above, but the expression is replaced with the result of its arithmetic evaluation. Example: echo "The average is $(( (a+b)/2 ))".

*, ?

Globs -- "wildcard" characters which match parts of filenames (e.g. ls *.txt).

~

Home directory — the tilde is a representation of a home directory. When alone or followed by a /, it means the current user's home directory; otherwise, a username must be specified (e.g. ls ~/Documents; cp ~john/.bashrc .).

&

Background -- when used at the end of a command, run the command in the background (do not wait for it to complete).

TASKS
Write a script that prints “Hello, World”, followed by a new line to the standard output.
ans: (echo "Hello, World")

Write a script that displays a confused smiley "(Ôo)'.
ans: (echo "\"(Ôo)'") is used. (\0) is used to prevent the next word or character from being interpreted.

Display the content of the /etc/passwd file.
ans: (cat /etc/passwd).

Display the content of /etc/passwd and /etc/hosts
ans: (cat /etc/passwd /etc/hosts).

Display the last 10 lines of /etc/passwd
ans: (tail /etc/passwd).

Display the first 10 lines of /etc/passwd
ans: (head /etc/passwd).

Write a script that displays the third line of the file iacta.
*The file iacta will be in the working directory
*You’re not allowed to use sed
ans: (head -3 iacta | tail -1).

Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.
ans: (echo -e "Best School" >> "\\*\\\\'\"Best School\"\\'\\\\*$\\?\\*\\*\\*\\*\\*:)").

Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.
ans: (ls -la >> ls_cwd_content).

Write a script that duplicates the last line of the file iacta
*The file iacta will be in the working directory
ans: (tail -1 iacta >> iacta).

Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
ans: (find . -type f -name '*.js' -delete).(find) is the path to look into. (-type f) is which file type which f means regular files. after (-name) is the name of the file. (-delete) is what u want to do with the files.

Write a script that counts the number of directories and sub-directories in the current directory.
*The current and parent directories should not be taken into account
*Hidden directories should be counted
ans: (find -mindepth 1 -type d |wc -l). (wc -l). (-mindepth) is look at minimum depth which means only the directory. (-type d) means file directory.

Create a script that displays the 10 newest files in the current directory.
*Requirements:
*One file per line
*Sorted from the newest to the oldest
ans: (ls -t |head) is used. (-t) means sort by modification time, newest first.

Create a script that takes a list of words as input and prints only words that appear exactly once.
*Input format: One line, one word
*Output format: One line, one word
*Words should be sorted
ans: (sort | uniq -u). (sort) means sort lines of text files.

Display lines containing the pattern “root” from the file /etc/passwd
ans: (egrep 'root' /etc/passwd)

Display the number of lines that contain the pattern “bin” in the file /etc/passwd
ans: (egrep -c 'bin' /etc/passwd)

Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.
ans: (egrep -A 3 'root' /etc/passwd)

Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.
ans: (egrep -v 'bin' /etc/passwd)

Display all lines of the file /etc/ssh/sshd_config starting with a letter.
*include capital letters as well
ans: (egrep ^[[:alpha:]] /etc/ssh/sshd_config)

Replace all characters A and c from input to Z and e respectively.
ans: (tr 'Ac' 'Ze')

Create a script that removes all letters c and C from input.
ans: (tr -d Cc)

Write a script that reverse its input.
ans: (rev)

Write a script that displays all users and their home directories, sorted by users.
*Based on the the /etc/passwd file
ans: (cut -f 1,6 -d ':' /etc/passwd | sort)

Write a command that finds all empty files and directories in the current directory and all sub-directories.

Only the names of the files and directories should be displayed (not the entire path)
Hidden files should be listed
One file name per line
The listing should end with a new line
You are not allowed to use basename, grep, egrep, fgrep or rgrep
ans: (find . -empty -printf "%f\n")

Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.
*Hidden files should be listed
*Only regular files (not directories) should be listed
*The names of the files should be displayed without their extensions
*The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
*One file name per line
*The listing should end with a new line
*You are not allowed to use basename, grep, egrep, fgrep or rgrep
ans: (find . -name "*.gif" -type f -printf "%f\n" | rev | cut -d. -f2- | rev | LC_ALL=C sort -f)

An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. Read more.
*Create a script that decodes acrostics that use the first letter of each line.
*The ‘decoded’ message has to end with a new line
You are not allowed to use grep, egrep, fgrep or rgrep
ans: (echo $(cut -c1 | tr -d "\n"))

Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.
*Order by number of requests, most active host or IP at the top
*You are not allowed to use grep, egrep, fgrep or rgrep
*Format:
ans: (tail -n +2 | sort | cut -f1 | uniq -c | sort -g -r | head -11 | tr -s " " | cut -d" " -f3)
