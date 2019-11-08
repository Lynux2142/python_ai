#!/bin/bash

MINICONDA_DIR="$HOME/Documents/miniconda3"
MINICONDA_PATH="$HOME/Documents/miniconda3/bin"
EXPORT="export PATH=\"$MINICONDA_PATH:\$PATH\""

function install()
{
	curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh > miniconda3.sh
	bash miniconda3.sh -b -p $MINICONDA_DIR
	TEST=`grep -c "$EXPORT" $HOME/.zshrc`
	if [ $TEST != "1" ]
	then
		echo $EXPORT >> $HOME/.zshrc
	fi
	export PATH="$MINICONDA_PATH:$PATH"
	rm -f miniconda3.sh
	echo "Python has been installed."
}

if [ -d $MINICONDA_DIR ]
then
	echo "Python is already installed, do you want to reinstall it?"
	echo -n "[yes|no]> "
	read RESPONCE
	if [[ $RESPONCE == "yes" ]]
	then
		rm -rf $MINICONDA_DIR
		echo "Python has been removed."
		install
	else
		echo "exit."
	fi
else
	install
fi
