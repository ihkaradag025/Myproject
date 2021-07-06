#!/bin/bash
read -p "input number: " number
if [[ $number -gt 10  ]]; then
	echo "$number büyük"
	if (( $number % 2 == 1 ))
	then
		echo "tek sayı"
	else
		echo "çift sayı"
	fi
else
	echo "10 dan büyük değil"
fi

