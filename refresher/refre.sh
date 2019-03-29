#!/bin/bash

if [ -d "$3" ]
then
	if [ -f "$3"/bin/activate ]
	then
		source "$3"/bin/activate
		deactivate
		
		rm -rf "$3"
		echo pls wait... rebuilding
		dir=$(pwd)
		cd "$2" # cd to parent folder of original virtualenv 
		virtualenv "$1" -p python3 --quiet 
		source "$1"/bin/activate
		cd "$dir"
		echo virtualenv "$1" re-initialized.
		
	fi
fi
exit 0