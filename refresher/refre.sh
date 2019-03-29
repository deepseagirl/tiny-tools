#!/bin/bash

if [ -d "$1" ]
then
	if [ -f "$1"/bin/activate ]
	then
		source "$1"/bin/activate
		deactivate
		
		rm -rf "$1"
		echo pls wait... rebuilding
		
		virtualenv "$1" -p python3 --quiet
		source "$1"/bin/activate
		echo virtualenv "$1" re-initialized.
		
	fi
fi
exit 0