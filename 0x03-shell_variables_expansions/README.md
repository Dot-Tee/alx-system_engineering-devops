shell expansion

The shell allows arithmetic expressions to be evaluated, as one of the shell expansions or by using the (( compound command, the let builtin, or the -i option to the declare builtin.

id++ id--
variable post-increment and post-decrement

++id --id
variable pre-increment and pre-decrement

- +
unary minus and plus

! ~
logical and bitwise negation

**
exponentiation

* / %
multiplication, division, remainder

+ -
addition, subtraction

<< >>
left and right bitwise shifts

<= >= < >
comparison

== !=
equality and inequality

&
bitwise AND

^
bitwise exclusive OR

|
bitwise OR

&&
logical AND

||
logical OR

expr ? expr : expr
conditional operator

= *= /= %= += -= <<= >>= &= ^= |=
assignment

expr1 , expr2
comma

The alias command makes it possible to launch any command or group of commands (inclusive of any options, arguments and redirection) by entering a pre-set string (i.e., sequence of characters).

That is, it allows a user to create simple names or abbreviations (even consisting of just a single character) for commands regardless of how complex the original commands are and then use them in the same way that ordinary commands are used.
e.g alias p="pwd"

TASKS
Create a script that creates an alias.
*Name: ls
*Value: rm *
ans: (alias ls="rm *") is used.

Create a script that prints hello user, where user is the current Linux user.
ans: (echo hello $USER) is used. ($) is a parameter expansion used to reveal the content in front of it.

Add /action to the PATH. /action should be the last directory the shell looks into when looking for a program.
ans: (export PATH=$PATH:/action)

Create a script that counts the number of directories in the PATH.
ans: (echo $PATH | tr -s ':' '\n' | wc -l)

Create a script that lists environment variables.
ans: (printenv)

Create a script that lists all local variables and environment variables, and functions.
ans: (set)

Create a script that creates a new local variable.
*Name: BEST
*Value: School
ans: (BEST="School")

Create a script that creates a new global variable.
*Name: BEST
*Value: School
ans: (export BEST="School")

Write a script that prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE, followed by a new line.
ans: (echo $(( 128 + $TRUEKNOWLEDGE )))

Write a script that prints the result of POWER divided by DIVIDE, followed by a new line.
*POWER and DIVIDE are environment variables
ans: (echo $(( $POWER / $DIVIDE )))

Write a script that displays the result of BREATH to the power LOVE
*BREATH and LOVE are environment variables
*The script should display the result, followed by a new line
ans: (echo $(( BREATH**LOVE )))

Write a script that converts a number from base 2 to base 10.
*The number in base 2 is stored in the environment variable BINARY
*The script should display the number in base 10, followed by a new line
ans: (echo $(( 2#$BINARY )))

Create a script that prints all possible combinations of two letters, except oo.
*Letters are lower cases, from a to z
*One combination per line
*The output should be alpha ordered, starting with aa
*Do not print oo
*Your script file should contain maximum 64 characters
ans: (echo {a..z}{a..z} | tr ' ' '\n' | grep -v "oo"
)

Write a script that prints a number with two decimal places, followed by a new line.
*The number will be stored in the environment variable NUM.
ans: (printf '%.2f\n' $NUM)

Write a script that converts a number from base 10 to base 16.
*The number in base 10 is stored in the environment variable DECIMAL
*The script should display the number in base 16, followed by a new line
ans: (printf '%x\n' $DECIMAL)

Write a script that encodes and decodes text using the rot13 encryption. Assume ASCII.
ans: (tr ` echo {a..z} | tr -d ' '` ` echo {n..z} $(echo {a..m}) | tr -d ' '` | tr ` echo {A..Z} | tr -d ' '` ` echo {N..Z} $(echo {A..M}) | tr -d ' '`)


Write a script that prints every other line from the input, starting with the first line.
ans: (perl -lne 'print if $. % 2 == 1')

Write a shell script that adds the two numbers stored in the environment variables WATER and STIR and prints the result.
*WATER is in base water
*STIR is in base stir.
*The result should be in base bestchol
ans: (echo $(printf %o $(($((5#$(echo $WATER | tr 'water' '01234'))) + $((5#$(echo $STIR | tr 'stir.' '01234'))))) | tr '01234567' 'bestchol'))