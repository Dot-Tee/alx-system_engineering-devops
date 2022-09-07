the file that contains the files of the command
The meaning of RTFM means Read The Fucking Manaul
#! Shebang
In computing, a shebang is the character sequence consisting of the characters number sign and exclamation mark (#!) at the beginning of a script. It is also called sharp-exclamation, sha-bang, hashbang,pound-bang,or hash-pling. (#!) When a text file with a shebang is used as if it is an executable in a Unix-like operating system, the program loader mechanism parses the rest of the file's initial line as an interpreter directive.
SHELL : the shell is a program that takes commands from the keyboard and gives them to the operating system to perform.
TERMINAL : It's a program called a terminal emulator. This is a program that opens a window and lets you interact with the shell. 

type - Display information about command type
which - Locate a command
help - Display reference page for shell builtin
man - Display an on-line command reference

Description of each script
Write a script that prints the absolute path name of the current working directory. ans: (pwd) is the command used to print the path name.
Display the contents list of your current directory. ans: (ls) is used to list content in the directory
Write a script that changes the working directory to the user’s home directory.
*You are not allowed to use any shell variables. 
ans: (cd ~) is used
Display current directory contents in a long format. ans: (ls -l) is used
Display current directory contents, including hidden files (starting with .). Use the long format. ans: (ls -la) is used. (-a) is used 1to display all hidden file including .
Display current directory contents.
*Long format
*with user and group IDs displayed numerically
*And hidden files (starting with .)
ans: (ls -lna) is used. (-n) is used to list numeric user and group ids.
Create a script that creates a directory named my_first_directory in the /tmp/ directory. 
ans: (mkdir /tmp/my_first_directory) is used to create a directory file into the /tmp/ directory.
Move the file betty from /tmp/ to /tmp/my_first_directory.
ans: (mv /tmp/betty /tmp/my_first_directory) is used to move file from one directory to the other.
Delete the file betty.
*The file betty is in /tmp/my_first_directory.
ans: (rm /tmp/my_first_directory/betty) is used to remove file from any location.
Delete the directory my_first_directory that is in the /tmp directory.
ans: (rmdir /tmp/my_first_directory) is used.
Write a script that changes the working directory to the previous one.
ans: (cd -) is used.
Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
ans: (ls -la . .. /boot) is used. The "." notation refers to the working directory itself and the ".." notation refers to the working directory's parent directory.
Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
ans: (file /tmp/iamafile) is used. (file) is used to print the type of file. file (classify a file's contents)
Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
ans: (ln -s /bin/ls __ls__) is used. (ln - ) make links between files. (-s) means symbolic link.
Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
*You can consider that all HTML files have the extension .html
ans: (cp -u *.html /tmp) is used. (cp) is used to copy file. (-u) --update, copy only when the SOURCE file is  newer  than  the destination of the file or when the destination file is missing. (*.html) is used for selecting specific files. 
Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.
*You can assume that the directory /tmp/u will exist when we will run your script.
ans: (mv [[:upper:]]* /tmp/u) is used.(upper) means upper case letter.
Create a script that deletes all files in the current working directory that end with the character ~.
ans: (rm *~)
Create a script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.
ans: (mkdir -p welcome/to/school) is used. (-p) makes parent directories if needed.
Write a command that lists all the files and directories of the current directory, separated by commas (,).
*Directory names should end with a slash (/)
*Files and directories starting with a dot (.) should be listed
*The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
*Only digits and letters are used to sort; Digits should come first
*You can assume that all the files we will test with will have at least one letter or one digit
*The listing should end with a new line
ans: (ls -map | sort -d) is used. (-d) is used to list directories themselves, not their content. (-m) is used to fill width with a comma separated list of entries. (--sort) used to sort by WORD instead of name.
Create a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.
ans: ()