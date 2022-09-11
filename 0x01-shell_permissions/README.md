it is all about shell permission

This lesson will cover the following commands:

chmod - modify file access rights
su - temporarily become the superuser
sudo - temporarily become the superuser
chown - change file ownership
chgrp - change a file's group ownership

File Permissions
On a Linux system, each file and directory is assigned access rights for the owner of the file, the members of a group of related users, and everybody else. Rights can be assigned to read a file, to write a file, and to execute a file (i.e., run the file as a prchmod
The chmod command is used to change the permissions of a file or directory. To use it, we specify the desired permission settings and the file or files that we wish to modify. There are two ways to specify the permissions. In this lesson we will focus on one of these, called the octal notation method.
rwx rwx rwx = 111 111 111
rw- rw- rw- = 110 110 110
rwx --- --- = 111 000 000

and so on...

rwx = 111 in binary = 7
rw- = 110 in binary = 6
r-x = 101 in binary = 5
r-- = 100 in binary = 4

755 : (rwxr-xr-x) The file's owner may read, write, and execute the file. All others may read and execute the file. This setting is common for programs that are used by all users.

TASKS
Create a script that switches the current user to the user betty.
*You should use exactly 8 characters for your command (+1 character for the new line)
*You can assume that the user betty will exist when we will run your script
ans: (sudo betty) is used to switch users.

Write a script that prints the effective username of the current user.
ans: (whoami) is used to print the username of the current user.

Write a script that prints all the groups the current user is part of.
ans: (groups) is used.

Write a script that changes the owner of the file hello to the user betty.
ans: (sudo chown betty hello) is used. Note that the name of the new file comes first.

Write a script that creates an empty file called hello.
ans: (touch hello) is used. (touch) is used to create an empty file.

Write a script that adds execute permission to the owner of the file hello.
ans: (chmod u+x hello) is used. (chmod u+x) is used to add execute permission to a file. (u) means user while (x) means execute (which is a permission).

Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
*The file hello will be in the working directory.
ans: (chmod 754 hello) is used. (754) means the binary number for creating permission (rwx...).

Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello
*The file hello will be in the working directory
*You are not allowed to use commas for this script
ans: (chmod +111 hello) is used. [Chmod 111 (chmod a+rwx,u-rw,g-rw,o-rw)] sets permissions so that, (U)ser / owner can't read, can't write and can execute. (G)roup can't read, can't write and can execute. (O)thers can't read, can't write and can execute. but (+) change it to (755).

Write a script that sets the permission to the file hello as follows:
*Owner: no permission at all
*Group: no permission at all
*Other users: all the permissions
ans (chmod 007 hello) is used. (0) means no permission while (7) means all permission.

Write a script that sets the mode of the file hello to this:
*-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
ans: (chmod 753 hello) is used.

Write a script that sets the mode of the file hello the same as olleh’s mode.
*The file hello will be in the working directory
*The file olleh will be in the working directory
ans: (chmod --reference olleh hello) is used.

Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.
ans: (chmod a+x */) is used. (a) means all(which is the user, group, others). (/) represent the directory.

Create a script that creates a directory called my_dir with permissions 751 in the working directory.
ans: (mkdir -m 751 my_dir) is used. (-m) means set file mode (as in chmod).

Write a script that changes the group owner to school for the file hello.
ans: (chgrp school hello) is used. (chgrp) means change group ownership.

Write a script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.
ans: (chown vincent:staff *) is used. (vincent:staff *) the changed owner names comes first before the new group name while * represent the working directory.

Write a script that changes the owner and the group owner of _hello to vincent and staff respectively.
*The file _hello is in the working directory
*The file _hello is a symbolic link.
ans: (chown -h vincent:staff _hello) is used. (-h) means affect  symbolic  links  instead  of any referenced file ( useful only on systems that can change the ownership of a symlink).

Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
ans: (chown --from=guillaume betty hello) is used.
[(--from) --from=CURRENT_OWNER:CURRENT_GROUP] change the owner and/or group of each file only if  its  c
urrent owner  and/or  group  match those specified here.  Either may be omitted, in which case a match is notrequired for  the  omitted attribute.
