#!/bin/sh

# Note that there must be no spaces around the "=" sign
MY_MASSAGE="hello world"


# Redirect the stderr to the same place (/dev/null) we are redirecting the stdout
> /dev/null 2>&1


# case
echo "Please talk to me"
while :
do
  read INPUT_VALUE
  case $INPUT_VALUE in
    hello)
      echo "Hello yourself!"
      ;;
    bye)
      echo "See you again!"
      break
      ;;
    *)
      echo "Sorry I don't understand!"
      ;;
  esac
done
echo "That's all."


# $#(number of parameters), $0(basename of the program), $1(first parameter)
echo "I was called with $# parameters"
echo "My name is $0"
echo "My first parameter is $1"
echo "My second parameter is $2"
echo "All parameters are $@"


# $? contains the exit value of the last run command
/usr/local/bin/my-command
if [ "$?" -ne "0" ]; then
  echo "Sorry, we had a problem there!"
fi


# IFS is interal field seperator
old_IFS="$IFS"
IFS=:
echo "Please input some data separated by colons ..."
read x y z
IFS=$old_IFS
echo "x is $x y is $y z is $z"


# Default value in brackets
echo "Your name is : ${myname:-John Doe}"


# A function will be called in a sub-shell if its output is piped somewhere else
# In the following example, the second echo command will output "x is 1" instead of "x is 2"
myfunc()
{
  echo "I was called as : $@"
  x=2
}

### Main script starts here

echo "Script was called with $@"
x=1
echo "x is $x"
myfunc 1 2 3 | tee out.log
echo "x is $x"


## write a recursive function
factorial() {
  if [ $1 -gt "1" ]; then
    i=`expr $1 - 1`
    j=`factorial $i`
    k=`expr $1 \* $j`
    echo $k
  else
    echo 1
  fi
}

echo "enter a number"
read i
factorial $i


# change suffix
rename_files() {
  FROM=$1
  TO=$2

  for i in *${FROM}
  do
    j=`basename $i $FROM`
    mv $i ${j}$TO
  done
}
