#!/bin/bash
read -p "enter a file name: " FILE
if [[ -e $FILE ]]
then
	        echo "$FILE dosya var"
	else
		        touch $FILE && echo "the file is created"
fi
